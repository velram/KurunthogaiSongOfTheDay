import twitter
import Back4App


# API key : mJTddacPiqxwwKqpCgkPEEc5a
# API secret key : URaMze2c3HGF8vUQh0k5BooXHaaeZGxFAkqCumFGkNjEEGY6kf
# Access token : 1068651616616701953-EvlNpFt1d8a4IbLufl0XDs0x07QSX4
# Access token secret : 7JYhhceh7i215CFTSVWlhAOdFOMMzYlL1wCcF6S4FgTrv

TWITTER_API_KEY = ''
TWITTER_API_SECRET_KEY = ''
TWITTER_ACCESS_TOKEN_KEY = ''
TWITTER_ACCESS_TOKEN_SECRET = ''

back4app_tools = Back4App.Back4AppTools()
todays_kurunthogai = back4app_tools.get_song()


# Access token : 134152924-UJBQnTFnkVRCy57U1N2pcizObVJyLxX7sjg5ZvCO
# Access token (secret) : 32uSIj2L9TJ4zDaHT54qvqraINCve03Vn9jmetaXvQQyl

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
