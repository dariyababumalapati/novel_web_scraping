import json
<<<<<<< HEAD
import pyperclip
import time

from autocopy import get_start_end_numbers, working_dictionary, update_chapter_number, next_tab, paste_and_enter, scroll_down, process_page, open_chrome

from bs4 import BeautifulSoup
from bs4_html_module import extract_chapter_html, convert_html_to_xhtml, replace_words_in_html

from epub_maker import EpubMaker
from share_file.g_drive_upolad import upload_f_to_g_drive

# Read from 'tk/jsons/ch_links.json'
with open('tk/jsons/ch_links_2.json', 'r', encoding='utf-8') as file:
    links_dict = json.load(file)

start_num = 451

stop_num = 453
cycles = 25

start_number, stop_number = get_start_end_numbers(start_num, stop_num, cycles)


work_dictionary = working_dictionary(links_dict, start_number, stop_number)

update_chapter_number(stop_number, cycles)
=======

import pyperclip

from autocopy import update_chapter_number, next_tab, paste_and_enter, process_page

from bs4 import BeautifulSoup
from bs4_html_module import extract_chapter_html, convert_html_to_xhtml, replace_words_in_html
import time


# Read from 'tk/jsons/ch_links.json'
with open('tk/jsons/ch_links.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

start_number = 55

stop_number = 80

update_chapter_number(stop_number)
>>>>>>> dca2e1185edd59f6ea541d656791141560c15841

replace_words = {'’': "'"}

chapters_data = {}

intial_url = 'https://www.mtlnovel.com/the-king/chapter-1-through-no-1/'

output_file = f'tk/jsons/chapters_data_{stop_number}.json'

<<<<<<< HEAD
# next_tab()

open_chrome()

for key, url in work_dictionary.items():
    pyperclip.copy(url)
    # print(url)
    paste_and_enter()
    time.sleep(2)
    scroll_down()
=======
next_tab()

for key, url in list(data.items())[start_number:stop_number+1]:
    pyperclip.copy(url)
    paste_and_enter()
    time.sleep(2)
>>>>>>> dca2e1185edd59f6ea541d656791141560c15841

    process_page()

    page_source = pyperclip.paste()
<<<<<<< HEAD
=======
    # with open(f'tk/htmls/{key}.html', 'w', encoding='utf-8') as file:
    #     file.write(page_source)
>>>>>>> dca2e1185edd59f6ea541d656791141560c15841
    soup = BeautifulSoup(page_source, "html.parser")
    html = extract_chapter_html(soup.prettify())
    html = replace_words_in_html(html, replace_words)
    xhtml = convert_html_to_xhtml(html)
    chapters_data[key] = xhtml


# Write chapters_data to f'tk/jsons/chapters_data{x}.json'
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(chapters_data, file, ensure_ascii=False, indent=4)

<<<<<<< HEAD
next_tab()

epub_file_name = f"tk_{stop_number}"

# Read from 'book_info.json'
with open('tk/book_info.json', 'r', encoding='utf-8') as file:
    book_info = json.load(file)

book_info['book_title'] = f"The King {stop_number}"
book_info['chapters_dict'] = chapters_data
book_info['epub_file_name'] = epub_file_name


# Create an instance of EpubMaker
the_king = EpubMaker()
the_king.make_epub(book_info)

# send the epub file to Google Drive
destination_file = f"{book_info['destination_directory']}/{epub_file_name}.epub"
drive_folder_id = book_info['drive_folder_id']

upload_f_to_g_drive(file_name=destination_file, folder_id=drive_folder_id)

=======
next_tab()
>>>>>>> dca2e1185edd59f6ea541d656791141560c15841
