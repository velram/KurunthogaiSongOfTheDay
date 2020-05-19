# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re


# TODO : fetch multiple URLs for various pages &
# dynamic rotation of URLs
# Set the URL you want to webscrape from
# url = 'https://ta.wikisource.org/s/s6' # Song 1 to 10

class Kurunthogai_Poems_Scrapper_Tools:
    def get_songs(self, beautiful_soup):
        song_paragraphs = beautiful_soup.find_all('dl')

        # Approach
        # Fetch the dl tag.
        # Fetch the first dd tag only - for song
        # Fetch

        # TODO - move this code to exclusive method - get_song()
        songs = []
        song_text = ""
        for song in song_paragraphs:
            # TODO - replace find_all() with find() - use null chk
            song_line_count = len(song.find_all('dd'))
            # Uncomment to debug
            # print("Song line count is : ", song_line_count)
            if (song != None and song_line_count >= 4):
                # print("\n\n Song paragraph is : \n\n " + song.text + " \n\n")
                song_text = song.text
            # print("\n\n Song text : \n" + song_text)
            # print("")

            dt_count = len(song.find_all('dt'))
            dd_count = len(song.find_all('dd'))
            # Uncomment to debug
            # print("Song line count is : ", song_line_count)
            if (None != song and 1 == dt_count and 1 == dd_count):
                # print("\n\n Song paragraph is : \n\n " + song.text + " \n\n")
                if (None != song.find('dd')):
                    author_name = song.find('dd').text
                    song_text = song_text + "\n~ " + author_name
                    # print("\n Song text with author name : \n" + song_text)
                    songs.append(song_text)
                # print("")
        return songs
