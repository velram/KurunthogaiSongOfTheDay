import back4app
import kurunthogai_poem_urls_scrapper
import kurunthogai_poems_scrapper
import kurunthogai_beautiful_soup_tools
import kurunthogai_tweeter
from local_config import *

FIRST_KURUNTHOGAI_PAGE_URL = 'https://ta.wikisource.org/s/s6'  # Song 1 to 10

back4app_tools = back4app.Back4AppTools()


def invoke_kurunthogai_web_scraping():
    kurunthogai_urls = scrape_all_kurunthogai_urls()
    kurunthogai_poems = []
    for kurunthogai_poem_url in kurunthogai_urls:
        print("poem URL : " + kurunthogai_poem_url)
        beautiful_soup_tools = kurunthogai_beautiful_soup_tools.Kurunthogai_Beautiful_Soup_Tools()
        kurunthogai_bs = beautiful_soup_tools.get_beautiful_soup_object(kurunthogai_poem_url)
        kurunthogai_poem_scrapper_tool = kurunthogai_poems_scrapper.Kurunthogai_Poems_Scrapper_Tools()
        temp_kurunthogai_poems = kurunthogai_poem_scrapper_tool.get_all_songs(kurunthogai_bs)
        kurunthogai_poems.extend(temp_kurunthogai_poems)
    return kurunthogai_poems


def scrape_all_kurunthogai_urls():
    kurunthogai_url_scrapper = kurunthogai_poem_urls_scrapper.Kurunthogai_URL_Scrapper()
    kurunthogai_urls = kurunthogai_url_scrapper.get_kurunthogai_page_links(FIRST_KURUNTHOGAI_PAGE_URL)
    return kurunthogai_urls


def invoke_store_kurunthogai_songs(kurunthogai_poems):
    back4app_tools.store_all_kurunthogai_songs(kurunthogai_poems)
    kurunthogai_song = back4app_tools.fetch_kurunthogai_song()
    print("பாடல் : \n ", kurunthogai_song)


def test_kurunthogai_scraping():
    temp_kurunthogai_poems = invoke_kurunthogai_web_scraping()
    for temp_kurunthogai_poem in temp_kurunthogai_poems:
        print("\n", temp_kurunthogai_poem)


def tweet_todays_kurunthogai():
    if 'True' == ENABLE_TWITTER_POSTING:
        print("Initiating Tweeting activity")
        kurunthogai_tweeter_tools = kurunthogai_tweeter.KurunthogaiTweeterTools()
        todays_kurunthogai_poem = back4app_tools.fetch_kurunthogai_song()
        kurunthogai_tweeter_tools.tweet_kurunthogai(todays_kurunthogai_poem)
        print("இன்றைய குறுந்தொகை : \n", todays_kurunthogai_poem)


if __name__ == "__main__":
    print("Enable tweeting : ", ENABLE_TWITTER_POSTING)
    print("Invoke DB loader : ", INVOKE_DB_LOADER)
    if 'True' == INVOKE_DB_LOADER:
        print('testing db loader')
        # scraped_kurunthogai_poems = invoke_kurunthogai_web_scraping()

        # print("\n\n Inside main page : \n ", scraped_kurunthogai_poems)

        # invoke_store_kurunthogai_songs(scraped_kurunthogai_poems)

    if 'True' == ENABLE_TWITTER_POSTING:
        print("Initiating Tweeting activity")
        kurunthogai_tweeter_tools = kurunthogai_tweeter.KurunthogaiTweeterTools()
        todays_kurunthogai_poem = back4app_tools.fetch_kurunthogai_song()
        kurunthogai_tweeter_tools.tweet_kurunthogai(todays_kurunthogai_poem)
        print("இன்றைய குறுந்தொகை : \n", todays_kurunthogai_poem)
        # test_kurunthogai_scraping()
