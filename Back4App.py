import requests
import json

# from local_settings import *

KURUNTHOGAI_POEMS_PARSE_URL = "https://parseapi.back4app.com/classes/KurunthogaiPoems"
POEM_TEXT_KEY = 'poem_text'
POEM_INDEX_KEY = 'poem_id'
POEM_AUTHOR_KEY = 'poem_author'
POEM_TWEETED_KEY = 'is_tweeted'

DAILY_ONE_KURUNTHOGAI_HASHTAG = '#தினமொரு_குறுந்தொகை'


def get_headers():
    return {
        'X-Parse-Application-Id': '',
        'X-Parse-REST-API-Key': '',
        'Content-Type': 'application/json'
    }


def update_status(object_id):
    url = "https://parseapi.back4app.com/classes/WordCorpus/" + object_id
    payload = {'status': True}
    header = get_headers()

    response = requests.put(url, data=json.dumps(payload), headers=header)
    print(response.text)
    return response.status_code


def get_sample_poem():
    return {
        "PoemIndex": 1,
        "PoemText": "செங்களம் படக்கொன் றவுணர்த் தேய்த்த செங்கோ லம்பிற் செங்கோட் டியானைக் கழல்தொடிச் சேஎய் குன்றம் "
                    "குருதிப் பூவின் குலைக்காந் தட்டே.",
        "PoemAuthor": "திப்புத் தோளார்"
    }


def get_kurunthogai_json(poem_index, poem_text, poem_author):
    kurunthogai_json = {
        POEM_INDEX_KEY: poem_index,
        POEM_TEXT_KEY: poem_text,
        POEM_AUTHOR_KEY: poem_author,
        POEM_TWEETED_KEY: False
    }
    return kurunthogai_json


class Back4AppTools():
    def get_song(self):
        header = get_headers()
        # url = "https://parseapi.back4app.com/classes/KurunthogaiPoems"
        data = requests.get(KURUNTHOGAI_POEMS_PARSE_URL, headers=header)
        json_response = data.json()

        song = ''
        if None != json_response:
            kurunthogai_poems = json_response['results'][0]
            poem_with_author = ('%s \n' %
                                (kurunthogai_poems[POEM_TEXT_KEY]))
            song = poem_with_author + '\n' + DAILY_ONE_KURUNTHOGAI_HASHTAG
        # update_status(results['object_id'])
        return song

    def populate_kurunthogai_in_db(self, poem_payload):
        # poem_payload = get_sample_poem()
        if None != poem_payload:
            print("\n json dump : ", json.dumps(poem_payload))
            kurunthogai_request_headers = get_headers()
            create_kurunthogai_status = requests.post(KURUNTHOGAI_POEMS_PARSE_URL,
                                                      data=json.dumps(poem_payload),
                                                      headers=kurunthogai_request_headers)
            print("Kurunthogai DB population activity status : ", create_kurunthogai_status)
        return create_kurunthogai_status

    def store_all_kurunthogai_songs(self, kurunthogai_poems):
        poem_index = 1
        kurunthogai_payloads = []
        for kurunthogai_poem in kurunthogai_poems:
            kurunthogai_poem_json_text = get_kurunthogai_json(poem_index, kurunthogai_poem, None)
            # kurunthogai_json_dump = json.dumps(kurunthogai_poem_json_text)
            print("\n\n பாடல் : ", poem_index, "\n", kurunthogai_poem_json_text)
            # print("JSON dump : ", kurunthogai_json_dump)
            # kurunthogai_payloads.extend(kurunthogai_json_dump)
            self.populate_kurunthogai_in_db(kurunthogai_poem_json_text)
            poem_index = poem_index + 1


if __name__ == "__main__":
    print("Try running daily_one_word.py first")
