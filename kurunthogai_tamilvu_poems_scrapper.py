from lxml import html
import requests
import kurunthogai_beautiful_soup_tools


# Fetch page object
# Fetch poem thinai type - DONE
# Fetch poem verses
# Fetch poet name
class TamilVU_Scrapper_Tools:
    # TODO update logic to fetch index only (call fetch_poem_thinai_type & parse the index number only)
    def fetch_poem_index(self, beautiful_soup_obj):
        poem_indexes = beautiful_soup_obj.find_all('div', attrs={"class": "subhead"})
        for poem_index in poem_indexes:
            print("poem index : ", poem_index.get_text())
        return poem_indexes

    def fetch_poem_thinai_type(self, beautiful_soup_obj):
        poem_thinai_types = beautiful_soup_obj.find_all('div', attrs={"class": "subhead"})
        for poem_thinai_type_ in poem_thinai_types:
            print("Poem Thinai Type  : ", poem_thinai_type_.get_text())
        return ''

    def fetch_poem_verses(self, beautiful_soup_obj):
        poem_elements = beautiful_soup_obj.find_all('div', attrs={"class": "poem"})
        for poem_element in poem_elements:
            # if not null or empty & not <font>
            if None != poem_element and None == poem_element.find('font'):
                print("Poem Thinai Type  : ", poem_element.get_text())
        return ''

    def fetch_poet_name(self):
        return ''


def test_kurunthogai_scraping(poem_page_url):
    beautiful_soup_tools = kurunthogai_beautiful_soup_tools.Kurunthogai_Beautiful_Soup_Tools()
    beautiful_soup_obj = beautiful_soup_tools.get_beautiful_soup_object(poem_page_url)
    tamilvu_scrapper_tools = TamilVU_Scrapper_Tools()
    # TamilVU_Scrapper_Tools.fetch_poem_index(tamilvu_scrapper_tools, beautiful_soup_obj)
    TamilVU_Scrapper_Tools.fetch_poem_verses(tamilvu_scrapper_tools, beautiful_soup_obj)


if __name__ == '__main__':
    poem_page_url = 'http://www.tamilvu.org/slet/l1220/l1220son.jsp?subid=3441'
    test_kurunthogai_scraping(poem_page_url)
