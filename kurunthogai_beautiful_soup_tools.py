import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re 


class Kurunthogai_Beautiful_Soup_Tools:
	def get_beautiful_soup_object(self, page_url):
		# Connect to the URL
		response = requests.get(page_url)
		# Parse HTML and save to BeautifulSoup object¶
		soup = BeautifulSoup(response.text, "html.parser")
		return soup 