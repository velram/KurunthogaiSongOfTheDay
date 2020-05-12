# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'https://ta.wikisource.org/s/s6'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

#print(soup)
# To download the whole data set, let's do a for loop through all a tags
#line_count = 1 #variable to track what line you are on
#print("before printing soup")
#print(soup.find_all('dd'))
#soup.find_all('p')[0].get_text()

song_paragraphs = soup.find_all('dl')

#Approach 
# Fetch the dl tag.
#Fetch the first dd tag only - for song 
#Fetch 


song_count = 1 #variable to track what line you are on
for song_paragraph in song_paragraphs:
	for song_line in song_paragraph.find_all('dd'):
	 	print(song_line.text)
	 	#print("song_count : " , song_count)
song_count +=1