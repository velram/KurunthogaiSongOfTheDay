import time

import requests
import json
from local_config import *

RESULTS_KEY = 'results'

KURUNTHOGAI_POEMS_DB_URL = "https://parseapi.back4app.com/classes/KurunthogaiPoems"
POEM_TEXT_KEY = 'kurunthogai_poem_loop_element'
POEM_INDEX_KEY = 'poem_id'
POEM_AUTHOR_KEY = 'poet_name'
POEM_TWEETED_KEY = 'is_tweeted'
OBJECT_ID_KEY = 'objectId'
SLASH_DELIMITER = '/'
KURUNTHOGAI_NON_TWEETED_FILTER_QUERY = '?where=%7B%22is_tweeted%22%3Afalse%7D'
DAILY_ONE_KURUNTHOGAI_HASHTAG = '#தினமொரு_குறுந்தொகை'


def get_headers():
    return {
        'X-Parse-Application-Id': BACK4APP_PARSE_API_APP_ID,
        'X-Parse-REST-API-Key': BACK4APP_PARSE_API_KEY,
        'Content-Type': 'application/json'
    }

def update_is_tweeted(kurunthogai_poem_object_id):
    kurunthogai_update_url = KURUNTHOGAI_POEMS_DB_URL + SLASH_DELIMITER + kurunthogai_poem_object_id
    kurunthogai_update_payload = {POEM_TWEETED_KEY: True}
    kurunthogai_req_headers = get_headers()
    kurunthogai_db_update_response = requests.put(kurunthogai_update_url,
                                                  data=json.dumps(kurunthogai_update_payload),
                                                  headers=kurunthogai_req_headers)
    print("Kurunthogai DB update status : ", kurunthogai_db_update_response)
    return kurunthogai_db_update_response


def get_sample_poem():
    return {
        "PoemIndex": 0,
        "PoemText": "செங்களம் படக்கொன் றவுணர்த் தேய்த்த செங்கோ லம்பிற் செங்கோட் டியானைக் கழல்தொடிச் சேஎய் குன்றம் "
                    "குருதிப் பூவின் குலைக்காந் தட்டே.",
        "PoemAuthor": "திப்புத் தோளார்"
    }


def get_kurunthogai_json(kurunthogai_poem):
    kurunthogai_json = {
        "index": kurunthogai_poem.poem_index,
        "poem_verses": kurunthogai_poem.poem_verses,
        "poet_name": kurunthogai_poem.poet_name,
        "poem_thinai_type": kurunthogai_poem.thinai_type,
        "is_tweeted": False
    }
    return kurunthogai_json


class TamilVUBack4AppTools():
    def fetch_kurunthogai_song(self):
        header = get_headers()
        kurunthogai_db_url_with_filter = KURUNTHOGAI_POEMS_DB_URL + KURUNTHOGAI_NON_TWEETED_FILTER_QUERY
        query_results = requests.get(kurunthogai_db_url_with_filter, headers=header)
        query_results_json = query_results.json()

        song = ''
        if query_results_json is not None:
            kurunthogai_poem_json_response = query_results_json[RESULTS_KEY][0]
            print('song to be updated is  : ', kurunthogai_poem_json_response)
            poem_with_author = ('%s \n' %
                                (kurunthogai_poem_json_response[POEM_TEXT_KEY]))
            song = poem_with_author + '\n' + DAILY_ONE_KURUNTHOGAI_HASHTAG
            print('song to be updated is  : ', kurunthogai_poem_json_response[OBJECT_ID_KEY])
            update_is_tweeted(kurunthogai_poem_json_response[OBJECT_ID_KEY])
        return song

    def populate_kurunthogai_in_db(self, poem_payload):
        if poem_payload is None:
            pass
        # poem_payload = get_sample_poem()
        else:
            print("\n json dump : ", json.dumps(poem_payload))
            kurunthogai_request_headers = get_headers()
            create_kurunthogai_status = requests.post(KURUNTHOGAI_POEMS_DB_URL,
                                                      data=json.dumps(poem_payload),
                                                      headers=kurunthogai_request_headers)
            print("Kurunthogai DB population activity status : ", create_kurunthogai_status)
        return create_kurunthogai_status

    def store_all_kurunthogai_songs(self, scraped_kurunthogai_poems):
        poem_index = 1
        kurunthogai_payloads = []
        for scraped_kurunthogai_poem in scraped_kurunthogai_poems:
            kurunthogai_poem_json = get_kurunthogai_json(scraped_kurunthogai_poem)
            # kurunthogai_json_dump = json.dumps(kurunthogai_poem_json)
            print("\n\n பாடல் : ", poem_index, "\n", kurunthogai_poem_json)
            print("JSON dump : ", kurunthogai_poem_json)
            kurunthogai_payloads.extend(kurunthogai_poem_json)
            time.sleep(1)
            self.populate_kurunthogai_in_db(kurunthogai_poem_json)
            poem_index = poem_index + 1
        print("Kurunthogai poems stored in DB : ", kurunthogai_payloads)
        print("Total number of poems stored in DB : ", poem_index)
        return kurunthogai_payloads


if __name__ == "__main__":
    print("Try running daily_one_word.py first")
