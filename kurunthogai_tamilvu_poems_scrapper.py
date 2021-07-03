import time
import kurunthogai_beautiful_soup_tools
import re


# Task list
# Fetch page object - DONE
# Fetch poem's thinai type - DONE
# Fetch poem verses - DONE
# Fetch poet name - WIP
class TamilVU_Scrapper_Tools:
    # TODO update logic to fetch index only (call fetch_poem_thinai_type & parse the index number only)
    def fetch_poem_indices(self, beautiful_soup_obj):
        time.sleep(3)
        poem_indices = []
        poem_elements = self.fetch_poem_thinai_types(beautiful_soup_obj)
        for poem_element in poem_elements:
            time.sleep(3)
            poem_indices.append(re.findall(r'-?\d+\d*', poem_element.get_text())[0])
        # print("poem index : ", poem_indices)
        return poem_indices

    # TODO - remove number from thinai types
    def fetch_poem_thinai_types(self, beautiful_soup_obj):
        time.sleep(3)
        poem_thinai_types = []
        poem_head_elements = beautiful_soup_obj.find_all('div', attrs={"class": "subhead"})
        for poem_head_element in poem_head_elements:
            time.sleep(3)
            print("Poem Thinai Type  : ", poem_head_element.get_text())
            poem_thinai_types.append(poem_head_element.get_text())
            break  # TODO - remove break stmt after testing
        return poem_head_elements

    def fetch_poem_verses(self, beautiful_soup_obj):
        time.sleep(3)
        poem_elements = beautiful_soup_obj.find_all('div', attrs={"class": "poem"})
        for poem_element in poem_elements:
            time.sleep(3)
            if poem_element is not None and poem_element.find('font') is None:
                print("Poem verse  : ", poem_element.get_text().strip())
        return ''

    def fetch_poet_names(self, beautiful_soup_obj):
        time.sleep(3)
        poem_elements = beautiful_soup_obj.find_all('div', attrs={"class": "poem"})
        poet_names = []
        for poem_element in poem_elements:
            time.sleep(3)
            if poem_element is not None and poem_element.find('font', attrs={"color": "#531a02"}) is not None:
                poem_explanation_and_poet_name = poem_element.find('font').get_text().strip()
                poet_name_delimiter = '-'
                poet_name = poem_explanation_and_poet_name.partition(poet_name_delimiter)[2].strip()
                poet_names.append(poet_name)
                print("poet name  : ", poet_name)
        print('poet names : ', poet_names)
        return poet_names

    # TODO - remove number from thinai types
    def fetch_kurunthogai(self, beautiful_soup_obj):
        time.sleep(3)
        poem_thinai_types = []
        poem_head_elements = beautiful_soup_obj.find_all('table')
        for poem_head_element in poem_head_elements:
            time.sleep(1)
            poem_index_thinai_type = poem_head_element.find('div', attrs={"class": "subhead"})
            if poem_index_thinai_type is not None:
                print("Kurunthogai element : ", poem_index_thinai_type.get_text())

            # print("Poem Thinai Type  : ", poem_head_element.get_text())
            # parent = poem_head_element.parent.parent.parent.parent.parent.parent.parent.parent.parent.parent.parent.parent.parent
            # print('parent element : ', parent)
            # poem_thinai_types.append(poem_head_element.get_text())
            # break  # TODO - remove break stmt after testing
        return poem_head_elements


def test_kurunthogai_scraping(poem_page_url):
    beautiful_soup_tools = kurunthogai_beautiful_soup_tools.Kurunthogai_Beautiful_Soup_Tools()
    beautiful_soup_obj = beautiful_soup_tools.get_beautiful_soup_object(poem_page_url)
    tamilvu_scrapper_tools = TamilVU_Scrapper_Tools()
    # TamilVU_Scrapper_Tools.fetch_poem_indices(tamilvu_scrapper_tools, beautiful_soup_obj)
    # TamilVU_Scrapper_Tools.fetch_poem_thinai_types(tamilvu_scrapper_tools, beautiful_soup_obj)
    # TamilVU_Scrapper_Tools.fetch_poem_verses(tamilvu_scrapper_tools, beautiful_soup_obj)
    # TamilVU_Scrapper_Tools.fetch_poet_names(tamilvu_scrapper_tools, beautiful_soup_obj)
    TamilVU_Scrapper_Tools.fetch_kurunthogai(tamilvu_scrapper_tools, beautiful_soup_obj)


if __name__ == '__main__':
    poem_page_url = 'http://www.tamilvu.org/slet/l1220/l1220son.jsp?subid=3441'
    test_kurunthogai_scraping(poem_page_url)
