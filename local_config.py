from os import environ
from dotenv import load_dotenv
from pathlib import Path  # python3 only

import os

env_path = Path('.') / '.env'
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

if __name__ == '__main__':
    print("Enable tweeting : ", ENABLE_TWITTER_POSTING)
