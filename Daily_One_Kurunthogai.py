import Back4App
import kurunthogai_poem_urls_scrapper


FIRST_KURUNTHOGAI_PAGE_URL = 'https://ta.wikisource.org/s/s6' # Song 1 to 10 

#back4app_tools = Back4App.Back4AppTools()
#kurunthogai_song = back4app_tools.get_song()

kurunthogai_url_scrapper = kurunthogai_poem_urls_scrapper.Kurunthogai_URL_Scrapper()
kurunthogai_urls = kurunthogai_url_scrapper.get_kurunthogai_page_links(FIRST_KURUNTHOGAI_PAGE_URL)

#print("kurunthogai_song : \n ", kurunthogai_song)
print("Kurunthogai URLs : ", kurunthogai_urls)