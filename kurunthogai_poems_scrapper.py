# Import libraries
import kurunthogai_beautiful_soup_tools
import kurunthogai_poem_urls_scrapper

# TODO : fetch multiple URLs for various pages &
# dynamic rotation of URLs
# Set the URL you want to webscrape from
# url = 'https://ta.wikisource.org/s/s6' # Song 1 to 10

class Kurunthogai_Poems_Scrapper_Tools:
    def get_all_songs(self, beautiful_soup):
        song_paragraphs = beautiful_soup.find_all('dl')

        # Approach
        # Fetch the dl tag.
        # Fetch the first dd tag only - for song
        # Fetch

        # TODO - move this code to exclusive method - get_song()
        songs = []
        song_text = ""
        for song in song_paragraphs:
            # TODO - replace find_all() with find() - use null chk
            song_line_count = len(song.find_all('dd'))
            # Uncomment to debug
            # print("Song line count is : ", song_line_count)
            # Expected tag structure for poem text is dl->dd (dd count should be minimum 4)
            if (song != None and song_line_count >= 4):
                # print("\n\n Song paragraph is : \n\n " + song.text + " \n\n")
                song_text = song.text
            # print("\n\n Song text : \n" + song_text)
            # print("")

            dt_count = len(song.find_all('dt'))
            dd_count = len(song.find_all('dd'))
            # Uncomment to debug
            # print("Song line count is : ", song_line_count)
            # Expected tag structure for poem author is dl->dd (dd count should be 1)
            if (None != song and 1 == dt_count and 1 == dd_count):
                # print("\n\n Song paragraph is : \n\n " + song.text + " \n\n")
                if (None != song.find('dd')):
                    author_name = song.find('dd').text
                    song_text = song_text + "\n~ " + author_name
                    # print("\n Song text with author name : \n" + song_text)
                    songs.append(song_text)
                # print("")
        return songs


def test_kurunthogai_scraping():
    print("Inside test kurunthogai scraping")
    kurunthogai_poem_url = 'https://ta.wikisource.org/s/s6'  # Song 1 to 10
    beautiful_soup_tools = kurunthogai_beautiful_soup_tools.Kurunthogai_Beautiful_Soup_Tools()
    kurunthogai_bs = beautiful_soup_tools.get_beautiful_soup_object(kurunthogai_poem_url)
    kurunthogai_scrapper_tools = Kurunthogai_Poems_Scrapper_Tools()
    temp_kurunthogai_poems = Kurunthogai_Poems_Scrapper_Tools.get_all_songs(kurunthogai_scrapper_tools, kurunthogai_bs)
    for temp_kurunthogai_poem in temp_kurunthogai_poems:
        print("\n", temp_kurunthogai_poem)


if __name__ == "__main__":
    test_kurunthogai_scraping()
