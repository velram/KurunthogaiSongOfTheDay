import twitter
from local_config import *


def connect_twitter():
    return twitter.Api(consumer_key=TWITTER_API_KEY,
                       consumer_secret=TWITTER_API_SECRET_KEY,
                       access_token_key=TWITTER_ACCESS_TOKEN_KEY,
                       access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)


class KurunthogaiTweeterTools:
    def tweet_kurunthogai(self, kurunthogai_poem):
        api = connect_twitter()
        print("Kurunthogai poem to be tweeted : ", kurunthogai_poem)
        twit_status = None
        if kurunthogai_poem is not None and len(kurunthogai_poem) <= 280:
            twit_status = api.PostUpdate(kurunthogai_poem)
            print(twit_status)
        else:
            print("TOO LONG: " + kurunthogai_poem)
        return twit_status
