# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re 

#TODO : fetch multiple URLs for various pages & 
# dynamic rotation of URLs
# Set the URL you want to webscrape from
#url = 'https://ta.wikisource.org/s/s6' # Song 1 to 10 
url = 'https://ta.wikisource.org/s/wp' #Song 41 to 50
#url = 'https://ta.wikisource.org/s/zc' #Song 101 to 110

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

#TODO - Scrap song number			
# Approach 
#  1. Tag hierarchy : h2 -> span -> class "mw_headline" -> id "பாடல்_"
#

headings = soup.find_all('h2')

for heading in headings:
	song_title = heading.find('span', class_ = 'mw-headline')
	if(None != song_title and None != re.findall(r'\d+', song_title.text)):
		song_number_text = re.findall(r'\d+', song_title.text)
		song_number = list(map(int, song_number_text))[0]
		print(song_number)
		#print(song_title.text)



songs = soup.find_all('dl')

#Approach 
# Fetch the dl tag.
#Fetch the first dd tag only - for song 
#Fetch 

#TODO - move this code to exclusive method - get_song()
for song in songs:
		#TODO - replace find_all() with find() - use null chk 
		song_line_count = len(song.find_all('dd'))
		#Uncomment to debug
		#print("Song line count is : ", song_line_count)
		if(song != None and song_line_count >= 4):
			#print("\n\n Song paragraph is : \n\n " + song.text + " \n\n")
			print("\n\n" + song.text)
			#print("")

		dt_count = len(song.find_all('dt'))
		dd_count = len(song.find_all('dd'))
		#Uncomment to debug
		#print("Song line count is : ", song_line_count)
		if(song != None and dt_count == 1 and dd_count == 1):
			#print("\n\n Song paragraph is : \n\n " + song.text + " \n\n")
			author_name = song.find('dd').text
			print("\n~ ", author_name)
			#print("")




#TODO find author name (for the 1-10 songs only) - remove this code later
for song in songs:
		#TODO - replace find_all() with find() - use null chk 
		if(song != None 
			and song.find('dd') != None 
			and song.find('dd').find('dl') != None 
			and song.find('dd').find('dl').find('dd') != None  
			and song.find('dd').find('dl').find('dd').find('dl') != None
			and song.find('dd').find('dl').find('dd').find('dl').find('dd') != None):
			song_author = song.find('dd').find('dl').find('dd').find('dl').find('dd')
			#print("song author is : ", song_author.text)