import time
import kurunthogai_beautiful_soup_tools
import re
from kurunthogai_popo import Kurunthogai


class TamilVUScrapperTools:

    @staticmethod
    def fetch_all_tables(beautiful_soup_obj):
        time.sleep(3)
        poem_thinai_types = []
        table_elements = beautiful_soup_obj.find_all('table')
        print("Array length is : ", len(table_elements))
        # print("Table at index 0 : ", table_elements[33])
        kurunthogai_poems = []
        for index in range(len(table_elements)):
            time.sleep(1)
            kurunthogai_poem = Kurunthogai('', '', '')
            poem_verses = ''
            if table_elements[index] is not None:
                not_parent_table = table_elements[index].find('a', attrs={"target": "_parent"}) is None
                not_head_div = table_elements[index].find('div', attrs={"class": "head"}) is None
                poem_header_exists = table_elements[index].find('div', attrs={"class": "subhead"}) is not None
                if not_parent_table and not_head_div and poem_header_exists:
                    # time.sleep(1)
                    poem_index_and_thinai_type = table_elements[index].get_text()
                    poem_index = re.findall(r'-?\d+\d*', poem_index_and_thinai_type)[0]
                    print("\nபாடல் எண் : ", poem_index)
                    kurunthogai_poem.poem_index = poem_index
                    poem_thinai_type = ''
                    if len(poem_index_and_thinai_type.split('.')) >= 1:
                        poem_thinai_type = poem_index_and_thinai_type.split('.')[1]
                        print('திணை வகை: ', poem_thinai_type)
                    poem_table = table_elements[index].findNext('table')
                    # print("பாடல் வரிகள் : \n ", poem_table)
                    poem_elements = poem_table.find_all('div', attrs={"class": "poem"})
                    # print('poem_elements : ', poem_elements)
                    print("பாடல் : \n")
                    for poem_element in poem_elements:
                        # time.sleep(2)
                        if poem_element is not None and poem_element.find('font') is None and\
                                poem_element.get_text().strip():
                            if poem_element.get_text().strip().find("\r\n") != -1:
                                poem_verse = poem_element.get_text().strip().replace("\r\n", "")
                                poem_verses = poem_verses + poem_verse + '\n'
                            else:
                                poem_verse = poem_element.get_text().strip()
                                poem_verses = poem_verses + poem_verse + '\n'
                    print(poem_verses)
                    poet_name_table = poem_table.findNext('table')
                    if poet_name_table is not None and \
                            poet_name_table.find('font', attrs={"color": "#531a02"}) is not None:
                        time.sleep(1)
                        poem_explanation_and_poet_name = poet_name_table.find('font').get_text().strip()
                        poet_name_delimiter = '-'
                        poet_name = poem_explanation_and_poet_name.partition(poet_name_delimiter)[2].strip()
                        print("இயற்றியவர்  : ", poet_name)


def trigger_kurunthogai_scraping(kurunthogai_page_url):
    beautiful_soup_tools = kurunthogai_beautiful_soup_tools.Kurunthogai_Beautiful_Soup_Tools()
    beautiful_soup_obj = beautiful_soup_tools.get_beautiful_soup_object(kurunthogai_page_url)
    TamilVUScrapperTools.fetch_all_tables(beautiful_soup_obj)


if __name__ == '__main__':
    for page_id in range(3402, 3442):
        poem_page_url = 'http://www.tamilvu.org/slet/l1220/l1220son.jsp?subid=' + str(page_id)
        print("Page to be scraped : ", poem_page_url)
        time.sleep(3)
        trigger_kurunthogai_scraping(poem_page_url)
        break
