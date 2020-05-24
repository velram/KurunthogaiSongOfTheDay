import Back4App
import json
import kurunthogai_poem_urls_scrapper
import kurunthogai_poems_scrapper
import kurunthogai_beautiful_soup_tools

FIRST_KURUNTHOGAI_PAGE_URL = 'https://ta.wikisource.org/s/s6'  # Song 1 to 10

back4app_tools = Back4App.Back4AppTools()

kurunthogai_url_scrapper = kurunthogai_poem_urls_scrapper.Kurunthogai_URL_Scrapper()
kurunthogai_urls = kurunthogai_url_scrapper.get_kurunthogai_page_links(FIRST_KURUNTHOGAI_PAGE_URL)

# print("Kurunthogai URLs : ", kurunthogai_urls)
kurunthogai_poems = []
for kurunthogai_poem_url in kurunthogai_urls:
    # print("poem URL : "+kurunthogai_poem_url)
    beautiful_soup_tools = kurunthogai_beautiful_soup_tools.Kurunthogai_Beautiful_Soup_Tools()
    kurunthogai_bs = beautiful_soup_tools.get_beautiful_soup_object(kurunthogai_poem_url)
    kurunthogai_poem_scrapper_tool = kurunthogai_poems_scrapper.Kurunthogai_Poems_Scrapper_Tools()
    temp_kurunthogai_poems = kurunthogai_poem_scrapper_tool.get_all_songs(kurunthogai_bs)
    kurunthogai_poems.extend(temp_kurunthogai_poems)
# print("\n\n Inside main page : \n ",kurunthogai_poems)

# print("\n\n Inside main page \n\n")

back4app_tools = Back4App.Back4AppTools()
back4app_tools.store_all_kurunthogai_songs(kurunthogai_poems)
# kurunthogai_song = back4app_tools.get_song()
# print("பாடல் : \n ", kurunthogai_song)
