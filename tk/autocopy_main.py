import json

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

replace_words = {'’': "'"}

chapters_data = {}

intial_url = 'https://www.mtlnovel.com/the-king/chapter-1-through-no-1/'

output_file = f'tk/jsons/chapters_data_{stop_number}.json'

next_tab()

for key, url in list(data.items())[start_number:stop_number+1]:
    pyperclip.copy(url)
    paste_and_enter()
    time.sleep(2)

    process_page()

    page_source = pyperclip.paste()
    # with open(f'tk/htmls/{key}.html', 'w', encoding='utf-8') as file:
    #     file.write(page_source)
    soup = BeautifulSoup(page_source, "html.parser")
    html = extract_chapter_html(soup.prettify())
    html = replace_words_in_html(html, replace_words)
    xhtml = convert_html_to_xhtml(html)
    chapters_data[key] = xhtml


# Write chapters_data to f'tk/jsons/chapters_data{x}.json'
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(chapters_data, file, ensure_ascii=False, indent=4)

next_tab()