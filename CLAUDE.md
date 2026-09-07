# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A Twitter/X bot that posts one poem per day from *Kurunthogai* (401 classical Tamil
Sangam poems). It scrapes the poems once into a Back4App (Parse) database, then a
scheduled job picks the next un-tweeted poem, formats it, and posts it.

## Commands

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt          # Python 3.6 (see runtime.txt)

python clock.py                          # run the blocking APScheduler daemon (this is the Heroku `clock` process)
python -m wikisource.todays_kurunthogai  # run the tweet job once (respects enable_twitter_posting)
python todays_kurunthogai_tamilvu.py     # alternate one-shot job (TamilVU stack; tweet call is currently commented out)
python kurunthogai_tamilvu_poems_scrapper.py  # scrape all 401 poems from TamilVU (one-time DB seeding)
python -m wikisource.kurunthogai_poems_scrapper   # scrape from Wikisource instead
python local_config.py                   # sanity-check that local.env is loading
```

There is no test suite, linter, or build step. Scripts are validated by running
them directly; most modules have an `if __name__ == '__main__'` smoke-test block.

## Configuration

`local_config.py` loads `local.env` (note: **not** `.env`) via python-dotenv and
re-exports every value as an UPPERCASE module constant. Nearly every module does
`from local_config import *`. On Heroku the same keys are set as config vars.

Gotchas:
- Boolean flags are compared as **strings**: `if 'True' == ENABLE_TWITTER_POSTING`.
  A value of `true` or `1` will silently disable posting.
- `*.env` is gitignored; `local.env` must be created by hand (keys listed in README.md).

## Architecture

There are **two parallel scrape → store → fetch → tweet stacks** that both target
the same Back4App class but use **incompatible field names**. This is mid-refactor;
be explicit about which one you are touching.

| Concern | Wikisource stack (older, still wired to `clock.py`) | TamilVU stack (newer, richer data) |
|---|---|---|
| Scraper | `wikisource/kurunthogai_poems_scrapper.py` (+ `kurunthogai_poem_urls_scrapper.py` for pagination) | `kurunthogai_tamilvu_poems_scrapper.py` |
| DB client | `wikisource/back4app.py` → `Back4AppTools` | `tamilvu_back4app.py` → `TamilVUBack4AppTools` |
| Job entrypoint | `wikisource/todays_kurunthogai.py` | `todays_kurunthogai_tamilvu.py` |
| Parse fields | `poem_id`, `poem_text`, `poem_author` | `index`, `poem_verses`, `poet_name`, `poem_thinai_type` |
| Tweet text | poem + hashtag | `index. verses \n~poet \n\n hashtag` (`build_poem_to_tweet`) |

`clock.py` → `wikisource.todays_kurunthogai.tweet_todays_kurunthogai()`, so the
**deployed path is the Wikisource stack**, but `KurunthogaiPoems.json` (the
canonical 401-poem dataset) uses the **TamilVU schema**. Reconciling these is the
main outstanding work (see `TODO_list.txt`).

Shared pieces:
- `kurunthogai_popo.py` — `Kurunthogai` plain object (index, thinai_type, verses, poet_name), produced by the TamilVU scraper.
- `kurunthogai_beautiful_soup_tools.py` — thin `requests` + BeautifulSoup fetch helper.
- `kurunthogai_tweeter.py` — `KurunthogaiTweeterTools.tweet_kurunthogai()`; refuses anything over 280 chars.
- `KurunthogaiPoems.json` — full dataset, also mirrored to the external `velram/kurunthogai-api` repo.

### Selection / dedup logic

`fetch_kurunthogai_song()` queries Parse with `where={"is_tweeted":false}` and takes
`results[0]` — the "next" poem is just the first un-tweeted row Parse returns.
After posting it should call `update_is_tweeted(objectId)` to flip the flag.
**That update call is currently commented out in `tamilvu_back4app.py`** (only the
Wikisource `back4app.py` still performs it), so the TamilVU one-shot never advances.

### Scraper specifics

- TamilVU: iterates page ids `subid=3402..3441` (`Kurunthogai_URLs_TamilVU.txt`),
  walks sibling `<table>` elements per poem, parses index/thinai from header text
  with regex, joins multi-line `<div class="poem">` fragments, extracts poet name
  after a `-` delimiter. Deliberately slow (`time.sleep` between pages/tables) to be polite.
- Wikisource: follows `span.searchaux#headernext` "next" links from `/s/s6` to
  paginate; parses `<dl>/<dd>` structure (≥4 `<dd>` = verse, `1 dt + 1 dd` = author).

## Deployment

Heroku, `clock` dyno (`Procfile`, `runtime.txt` pins python-3.6.10). All `local.env`
keys must be set as Heroku config vars.
