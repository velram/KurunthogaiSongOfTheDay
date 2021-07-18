from os import environ
from dotenv import load_dotenv
from pathlib import Path  # python3 only

import os

# env_path = Path('.') / '.env'
env_path = Path('local.env')
load_dotenv(dotenv_path=env_path)
SECRET_KEY = os.getenv("enable_twitter_posting")

ENABLE_TWITTER_POSTING = os.getenv('enable_twitter_posting')
INVOKE_DB_LOADER = os.getenv('invoke_db_loader')

# Twitter API configuration
TWITTER_API_KEY = os.getenv('twitter_api_key')
TWITTER_API_SECRET_KEY = os.getenv('twitter_api_secret_key')
TWITTER_ACCESS_TOKEN_KEY = os.getenv('twitter_access_token_key')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('twitter_access_token_secret')

# Back4App configuration
BACK4APP_PARSE_API_KEY = os.getenv('back_4_app_api_key')
BACK4APP_PARSE_API_APP_ID = os.getenv('back_4_app_parse_application_id')
BACK4APP_KURUNTHOGAI_DB_URL = os.getenv('back4app_kurunthogai_db_url')
# Tweet schedule

TWEET_SCHEDULE_DAY = os.getenv('tweet_schedule_day')
TWEET_SCHEDULE_HOUR = os.getenv('tweet_schedule_hour')
TWEET_SCHEDULE_MINUTE = os.getenv('tweet_schedule_minute')

if __name__ == '__main__':
    # print("Enable tweeting : ", ENABLE_TWITTER_POSTING)
    # print("Tweet schedule hour tweeting : ", int(TWEET_SCHEDULE_HOUR))
    print('Parse API key : ', BACK4APP_PARSE_API_KEY)
