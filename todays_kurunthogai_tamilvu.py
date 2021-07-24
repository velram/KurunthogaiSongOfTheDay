import tamilvu_back4app
from wikisource import kurunthogai_poem_urls_scrapper
import kurunthogai_tweeter
from local_config import *
from kurunthogai_tamilvu_poems_scrapper import TamilVUScrapperTools

tamilvu_back4app_tools = tamilvu_back4app.TamilVUBack4AppTools()


def tweet_todays_kurunthogai():
    if 'True' == ENABLE_TWITTER_POSTING:
        print("Initiating Tweeting activity")
        kurunthogai_tweeter_tools = kurunthogai_tweeter.KurunthogaiTweeterTools()
        todays_kurunthogai_poem = tamilvu_back4app_tools.fetch_kurunthogai_song()
        # kurunthogai_tweeter_tools.tweet_kurunthogai(todays_kurunthogai_poem)
        print("இன்றைய குறுந்தொகை : \n", todays_kurunthogai_poem)


if __name__ == "__main__":
    print("Enable tweeting : ", ENABLE_TWITTER_POSTING)
    if 'True' == ENABLE_TWITTER_POSTING:
        print("Initiating Tweeting activity")
        kurunthogai_tweeter_tools = kurunthogai_tweeter.KurunthogaiTweeterTools()
        todays_kurunthogai_poem = tamilvu_back4app_tools.fetch_kurunthogai_song()
        kurunthogai_tweeter_tools.tweet_kurunthogai(todays_kurunthogai_poem)
        print("இன்றைய குறுந்தொகை : \n", todays_kurunthogai_poem)
        # test_kurunthogai_scraping()
