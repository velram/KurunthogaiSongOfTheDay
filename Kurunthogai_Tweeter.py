import twitter
import Back4App

TWITTER_API_KEY = ''
TWITTER_API_SECRET_KEY = ''
TWITTER_ACCESS_TOKEN_KEY = ''
TWITTER_ACCESS_TOKEN_SECRET = ''

back4app_tools = Back4App.Back4AppTools()
todays_kurunthogai = back4app_tools.get_song()

def connect_twitter():
    return twitter.Api(consumer_key=TWITTER_API_KEY,
                       consumer_secret=TWITTER_API_SECRET_KEY,
                       access_token_key=TWITTER_ACCESS_TOKEN_KEY,
                       access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)


if __name__ == "__main__":
    api = connect_twitter()

    if todays_kurunthogai is not None and len(todays_kurunthogai) <= 280:
        twitStatus = api.PostUpdate(todays_kurunthogai)
        print(twitStatus)
    else:
        print("TOO LONG: " + todays_kurunthogai)
