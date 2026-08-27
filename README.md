# Kurunthogai Song of the Day

A Twitter/X bot that posts one poem from *Kurunthogai* — a classical Tamil
anthology of 401 Sangam-era love poems — every day.

## Features

- Publishes one poem daily, with its index, verses, poet's name and *thinai*
  (landscape) type, plus the `#தினமொரு_குறுந்தொகை` hashtag.
- Scrapes and normalises all 401 poems from
  [Tamil Virtual University](http://www.tamilvu.org) and
  [Tamil Wikisource](https://ta.wikisource.org).
- Tracks progress in a hosted database so no poem repeats until the cycle ends.
- Runs unattended on a configurable daily schedule.

## How it works

1. **Scrape** — `kurunthogai_tamilvu_poems_scrapper.py` parses each source page
   into `Kurunthogai` objects (`kurunthogai_popo.py`).
2. **Store** — `tamilvu_back4app.py` writes every poem to a Back4App (Parse)
   class with an `is_tweeted` flag.
3. **Select** — the bot queries the first poem where `is_tweeted = false` and
   formats it for posting.
4. **Post** — `kurunthogai_tweeter.py` publishes it via the Twitter API and the
   record is marked as tweeted.
5. **Schedule** — `clock.py` uses APScheduler to trigger the job at the
   configured day/hour/minute.

## Tech stack

Python 3.6 · requests · BeautifulSoup 4 · python-twitter · APScheduler ·
python-dotenv · Back4App (Parse) · Heroku

## Setup

```bash
git clone https://github.com/velram/KurunthogaiSongOfTheDay.git
cd KurunthogaiSongOfTheDay
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Create a `local.env` file (loaded by `local_config.py`; never commit it):

```env
enable_twitter_posting=True
invoke_db_loader=False

twitter_api_key=...
twitter_api_secret_key=...
twitter_access_token_key=...
twitter_access_token_secret=...

back_4_app_parse_application_id=...
back_4_app_api_key=...
back4app_kurunthogai_db_url=https://parseapi.back4app.com/classes/KurunthogaiPoems

twitter_hashtag=#தினமொரு_குறுந்தொகை
tweet_schedule_day=*
tweet_schedule_hour=8
tweet_schedule_minute=0
```

## Usage

```bash
# Post today's poem once
python todays_kurunthogai_tamilvu.py

# Run the scheduler (long-running)
python clock.py

# One-time: scrape sources and load the database
python kurunthogai_tamilvu_poems_scrapper.py   # set invoke_db_loader=True
```

## Deployment

Deploys to Heroku as a `clock` process (see `Procfile` and `runtime.txt`).
Set every key from `local.env` as a Heroku config var.

## Data

The full dataset is published as JSON in
[kurunthogai-api](https://github.com/velram/kurunthogai-api)
(`KurunthogaiPoems.json`, also included here).

## License

Released under the [GNU GPL v3.0](LICENSE).

## Credits

Inspired by
[DailyOneTamilWord](https://github.com/KaniyamFoundation/DailyOneTamilWord)
by [Khaleel Jageer](https://github.com/khaleeljageer) and the Kaniyam
Foundation. Poem texts courtesy of Tamil Virtual University and Tamil
Wikisource.
