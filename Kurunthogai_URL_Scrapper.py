# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re 
import kurunthogai_beautiful_soup_tools

WIKISOURCE_URL_ROOT = 'https://ta.wikisource.org'

#TODO : fetch multiple URLs for various pages & 
# dynamic rotation of URLs
# Set the URL you want to webscrape from
FIRST_KURUNTHOGAI_PAGE_URL = 'https://ta.wikisource.org/s/s6' # Song 1 to 10 
#url = 'https://ta.wikisource.org/s/wp' #Song 41 to 50
#url = 'https://ta.wikisource.org/s/zc' #Song 101 to 110


class Kurunthogai_URL_Scrapper:

def get_beautiful_soup_object(page_url):
	# Connect to the URL
	response = requests.get(page_url)

	# Parse HTML and save to BeautifulSoup object¶
	soup = BeautifulSoup(response.text, "html.parser")
	return soup 


#TODO - Fetch Song URLs
#Approach 
# 1. Initialize the 1st URL
# 2. Read the next song list URL
# 3. If it's not empty use it else break the loop

#Tag hierarchy for next song list 
# span -> class='searchaux' id='headernext'

def get_kurunthogai_page_links(first_page_url):

	next_song_absolute_url = first_page_url
	kurunthogai_song_urls = []
	kurunthogai_bs_tools = kurunthogai_beautiful_soup_tools.Kurunthogai_Beautiful_Soup_Tools() 
	soup_object = get_beautiful_soup_object(first_page_url)

	while None != next_song_absolute_url:
		next_song_list_container = soup_object.find('span', attrs={"class" : "searchaux", "id" :"headernext"})
		if(None != next_song_list_container and None != next_song_list_container.find('a')):
			next_song_list_link_text = next_song_list_container.find('a').text
			next_song_list_path = next_song_list_container.find('a')['href']
			#print("next song list text : " + next_song_list_link_text + " path : "+next_song_list_path)
			if(None != next_song_list_path):
				next_song_absolute_url = WIKISOURCE_URL_ROOT + next_song_list_path
				kurunthogai_song_urls.append(next_song_absolute_url)
				print(next_song_list_link_text + " : " + next_song_absolute_url + "\n")
				soup_object = get_beautiful_soup_object(next_song_absolute_url)
			if(None == next_song_absolute_url or first_page_url == next_song_absolute_url):
				print("No more next page")
				return
		else:
			print("Empty song container or No links found")
			break
	return kurunthogai_song_urls			

kurunthogai_poem_urls = get_kurunthogai_page_links(FIRST_KURUNTHOGAI_PAGE_URL)

print("Kurunthogai URLs : ", kurunthogai_poem_urls)