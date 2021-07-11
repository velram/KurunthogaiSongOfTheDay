import time
import kurunthogai_beautiful_soup_tools
import re
from kurunthogai_popo import Kurunthogai


# Task list
# Fetch page object - DONE
# Fetch poem's thinai type - DONE
# Fetch poem verses - DONE
# Fetch poet name - WIP
class TamilVUScrapperTools:
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
            # break  # TODO - remove break stmt after testing
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

            poem_verse = poem_head_element.find('div', attrs={"class": "poem"})

            if poem_verse is not None and poem_verse.find('font') is None:
                print("Poem verse : ", poem_verse.get_text())

            # print("Poem Thinai Type  : ", poem_head_element.get_text())
            # parent = poem_head_element.parent.parent.parent.parent.parent.parent.parent.parent.parent.parent.parent.parent.parent
            # print('parent element : ', parent)
            # poem_thinai_types.append(poem_head_element.get_text())
            # break  # TODO - remove break stmt after testing
        return poem_head_elements

    @staticmethod
    def fetch_all_tables(beautiful_soup_obj):
        time.sleep(3)
        poem_thinai_types = []
        table_elements = beautiful_soup_obj.find_all('table')
        print("Array length is : ", len(table_elements))
        # print("Table at index 0 : ", table_elements[33])
        # TODO
        # - conditions - table not target
        # - table not "head"
        # Read table element of index
        # Read next table element of poem
        # Read next table element of poet
        kurunthogai_poems = []
        for index in range(len(table_elements) - 3):
            if table_elements[index] is not None:
                not_parent_table = table_elements[index].find('a', attrs={"target": "_parent"}) is None
                not_head_div = table_elements[index].find('div', attrs={"class": "head"}) is None
                poem_header_exists = table_elements[index].find('div', attrs={"class": "subhead"}) is not None
                if not_parent_table and not_head_div and poem_header_exists:
                    time.sleep(1)
                    poem_header_text = table_elements[index].get_text()
                    print("\nபாடல் எண் & திணை வகை: ", poem_header_text)
                    poem_table = table_elements[index].findNext('table')
                    # print("பாடல் வரிகள் : \n ", poem_table)
                    poem_elements = poem_table.find_all('div', attrs={"class": "poem"})
                    # print('poem_elements : ', poem_elements)
                    print("பாடல் : \n")
                    for poem_element in poem_elements:
                        time.sleep(3)
                        if poem_element is not None and poem_element.find('font') is None:
                            print(poem_element.get_text().strip())
                    # break
                    poet_name_table = poem_table.findNext('table')
                    # print("poet_name : ", poet_name_table)
                    if poet_name_table is not None and \
                            poet_name_table.find('font', attrs={"color": "#531a02"}) is not None:
                        time.sleep(1)
                        poem_explanation_and_poet_name = poet_name_table.find('font').get_text().strip()
                        poet_name_delimiter = '-'
                        poet_name = poem_explanation_and_poet_name.partition(poet_name_delimiter)[2].strip()
                        # poet_names.append(poet_name)
                        print("\n இயற்றியவர்  : ", poet_name)

                    # print("இயற்றியவர் : \n ", poet_name_table)

def test_kurunthogai_scraping(poem_page_url):
    beautiful_soup_tools = kurunthogai_beautiful_soup_tools.Kurunthogai_Beautiful_Soup_Tools()
    beautiful_soup_obj = beautiful_soup_tools.get_beautiful_soup_object(poem_page_url)
    tamilvu_scrapper_tools = TamilVUScrapperTools()
    # TamilVUScrapperTools.fetch_poem_indices(tamilvu_scrapper_tools, beautiful_soup_obj)
    # TamilVUScrapperTools.fetch_poem_thinai_types(tamilvu_scrapper_tools, beautiful_soup_obj)
    # TamilVUScrapperTools.fetch_poem_verses(tamilvu_scrapper_tools, beautiful_soup_obj)
    # TamilVUScrapperTools.fetch_poet_names(tamilvu_scrapper_tools, beautiful_soup_obj)
    # TamilVUScrapperTools.fetch_kurunthogai(tamilvu_scrapper_tools, beautiful_soup_obj)
    TamilVUScrapperTools.fetch_all_tables(beautiful_soup_obj)


if __name__ == '__main__':
    poem_page_url = 'http://www.tamilvu.org/slet/l1220/l1220son.jsp?subid=3441'
    test_kurunthogai_scraping(poem_page_url)
