import tamilvu_back4app
from wikisource import kurunthogai_poem_urls_scrapper
import kurunthogai_tweeter
from local_config import *
from kurunthogai_tamilvu_poems_scrapper import TamilVUScrapperTools

FIRST_KURUNTHOGAI_PAGE_URL = 'http://www.tamilvu.org/slet/l1220/l1220son.jsp?subid='  # Song 1 to 10

tamilvu_back4app_tools = tamilvu_back4app.TamilVUBack4AppTools()


def invoke_kurunthogai_web_scraping():
    kurunthogai_tamilvu_poems_scrapper = TamilVUScrapperTools()
    kurunthogai_poems = kurunthogai_tamilvu_poems_scrapper.initiate_kurunthogai_scraping()
    return kurunthogai_poems


def scrape_all_kurunthogai_urls():
    kurunthogai_url_scrapper = kurunthogai_poem_urls_scrapper.Kurunthogai_URL_Scrapper()
    kurunthogai_urls = kurunthogai_url_scrapper.get_kurunthogai_page_links(FIRST_KURUNTHOGAI_PAGE_URL)
    return kurunthogai_urls


def invoke_store_kurunthogai_songs(kurunthogai_poems):
    tamilvu_back4app_tools.store_all_kurunthogai_songs(kurunthogai_poems)
    # kurunthogai_song = tamilvu_back4app_tools.fetch_kurunthogai_song()
    # print("பாடல் : \n ", kurunthogai_song)


def test_kurunthogai_scraping():
    temp_kurunthogai_poems = invoke_kurunthogai_web_scraping()
    for temp_kurunthogai_poem in temp_kurunthogai_poems:
        print("\n", temp_kurunthogai_poem)


def tweet_todays_kurunthogai():
    if 'True' == ENABLE_TWITTER_POSTING:
        print("Initiating Tweeting activity")
        kurunthogai_tweeter_tools = kurunthogai_tweeter.KurunthogaiTweeterTools()
        todays_kurunthogai_poem = tamilvu_back4app_tools.fetch_kurunthogai_song()
        kurunthogai_tweeter_tools.tweet_kurunthogai(todays_kurunthogai_poem)
        print("இன்றைய குறுந்தொகை : \n", todays_kurunthogai_poem)


if __name__ == "__main__":
    print("Enable tweeting : ", ENABLE_TWITTER_POSTING)
    print("Invoke DB loader : ", INVOKE_DB_LOADER)
    if INVOKE_DB_LOADER:
        print('testing db loader')
        scraped_kurunthogai_poems = invoke_kurunthogai_web_scraping()

        print("\n\n Inside main page : \n ", scraped_kurunthogai_poems)

        invoke_store_kurunthogai_songs(scraped_kurunthogai_poems)

    # if 'True' == ENABLE_TWITTER_POSTING:
    #     print("Initiating Tweeting activity")
    #     kurunthogai_tweeter_tools = kurunthogai_tweeter.KurunthogaiTweeterTools()
    #     todays_kurunthogai_poem = tamilvu_back4app_tools.fetch_kurunthogai_song()
    #     kurunthogai_tweeter_tools.tweet_kurunthogai(todays_kurunthogai_poem)
    #     print("இன்றைய குறுந்தொகை : \n", todays_kurunthogai_poem)
    #     # test_kurunthogai_scraping()
