import json
import pyperclip
import time

from autocopy import get_start_end_numbers, working_dictionary, update_chapter_number, next_tab, paste_and_enter, scroll_down, process_page, open_chrome

from bs4 import BeautifulSoup
from bs4_html_module import extract_uu_chapter_html, convert_html_to_xhtml


start_number = 501

stop_number = 525


output_file = f'tk/jsons/chapters_data_{stop_number}.json'

# next_tab()

chapters_data = {}

open_chrome()

print(start_number, stop_number)

for i in range(start_number, stop_number+1):
    url = f'https://m.uuks.org/b/57664/72080{i}.html'
    key = f"Chapter {i}"
    pyperclip.copy(url)
    # print(url)
    paste_and_enter()
    time.sleep(2)
    scroll_down()

    process_page()

    page_source = pyperclip.paste()
    soup = BeautifulSoup(page_source, "html.parser")
    html = extract_uu_chapter_html(soup.prettify())
    xhtml = convert_html_to_xhtml(html)
    chapters_data[key] = xhtml


# Write chapters_data to f'tk/jsons/chapters_data{x}.json'
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(chapters_data, file, ensure_ascii=False, indent=4)

next_tab()

