import json
from bs4 import BeautifulSoup
from bs4_html_module import extract_chapter_html, convert_html_to_xhtml, replace_words_in_html
import time

import os
import sys

import logging

# Add the root directory to the system path
root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_directory)

from logging_config import setup_logging


from extract_html_mtl import raw_driver
from epub.epub_maker import EpubMaker
from share_file.g_drive_upolad import upload_f_to_g_drive

# Initialize logging
setup_logging()
logger = logging.getLogger(__name__)


# Read from 'tk/jsons/ch_links.json'
with open('mlt/jsons/ch_links.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

start_number = 1

stop_number = 100


replace_words = {'’': "'"}

chapters_data = {}

intial_url = 'https://www.mtlnovel.com/i-want-to-be-qin-ii/chapter-1-gongzi-gao/'

output_file = f'mlt/jsons/chapters_data_{stop_number}.json'


for key, url in list(data.items())[:stop_number+1]:
    driver = raw_driver(url)
    driver.implicitly_wait(10)
    page_source = driver.page_source

    soup = BeautifulSoup(page_source, "html.parser")
    # print(soup.prettify())
    html = extract_chapter_html(soup.prettify())
    html = replace_words_in_html(html, replace_words)
    xhtml = convert_html_to_xhtml(html)
    chapters_data[key] = xhtml


# Write chapters_data to f'tk/jsons/chapters_data{x}.json'
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(chapters_data, file, ensure_ascii=False, indent=4)

driver.quit()


# epub part

epub_file_name = f"qin_{stop_number}"

# Read from 'book_info.json'
with open('mlt/book_info.json', 'r', encoding='utf-8') as file:
    book_info = json.load(file)

book_info['book_title'] = f"qin {stop_number}"
book_info['chapters_dict'] = chapters_data
book_info['epub_file_name'] = epub_file_name


# Create an instance of EpubMaker
the_king = EpubMaker()
the_king.make_epub(book_info)                       

# send the epub file to Google Drive
destination_file = f"{book_info['destination_directory']}/{epub_file_name}.epub"
drive_folder_id = book_info['drive_folder_id']

upload_f_to_g_drive(file_name=destination_file, folder_id=drive_folder_id)

