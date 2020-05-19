import requests
import json


# from local_settings import *


def get_headers():
    return {
        'X-Parse-Application-Id': '',
        'X-Parse-REST-API-Key': '',
        'Content-Type': 'application/json'
    }


def update_status(objectId):
    url = "https://parseapi.back4app.com/classes/WordCorpus/" + objectId
    payload = {'status': True}
    header = get_headers()

    response = requests.put(url, data=json.dumps(payload), headers=header)
    print(response.text)
    return response.status_code


class Back4AppTools():
    def get_song(self):
        header = get_headers()
        url = "https://parseapi.back4app.com/classes/KurunthogaiPoems"
        data = requests.get(url, headers=header)
        json_response = data.json()

        kurunthogai_poems = json_response['results'][0]
        poem_with_author = ('%s \n ~ %s' %
                            (kurunthogai_poems['poem_text'], kurunthogai_poems['poem_author']))
        # update_status(results['objectId'])
        tags = '\n#தினமொரு_குறுந்தொகை'
        return poem_with_author + tags


if __name__ == "__main__":
    print("Try running daily_one_word.py first")
