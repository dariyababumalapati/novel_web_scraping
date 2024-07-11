import json
import pyperclip
import time
import os
import sys

import logging

# Add the root directory to the system path
root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_directory)

from logging_config import setup_logging

from extract_html_module_tk import initiate_driver, raw_driver, click_consent_button, wait_to_translate, scroll_to_bottom, scroll_to_top, copy_full_html
# from autocopy import open_chrome, paste_and_enter, scroll_down, copy_outer_html, contains_simplified_chinese, refresh_page, next_tab

from bs4 import BeautifulSoup
from bs4_html_module import check_chinese_text, extract_uu_chapter_html, convert_html_to_xhtml, replace_words_in_html
from utils import slice_dict, save_html

from epub_maker import EpubMaker
from share_file.g_drive_upolad import upload_f_to_g_drive

# Initialize logging
setup_logging()
logger = logging.getLogger(__name__)

start_number = 601

stop_number = start_number + 49


raw_json = f'tk/jsons/raw/raw_data_{stop_number}.json'

raw_data = {}

primary_url = 'https://m.uuks.org/b/57664/72080526.html'



try:
    raw_driver = raw_driver(primary_url)
    # raw_driver.maximize_window()
    click_consent_button(raw_driver)
    time.sleep(1)
    logger.info(f"Driver initialized and navigated to {primary_url}")
except Exception as e:
    logger.error(f"Error initializing driver or navigating to primary URL: {e}")
    raise

for i in range(start_number, stop_number+1):
    url = f'https://m.uuks.org/b/57664/72080{i}.html'
    key = f"Chapter {i}"

    try:
        raw_driver.get(url)
        logger.info(f"Navigated to {url}")
        outer_html = copy_full_html(raw_driver)
        # save_html(outer_html, f'tk/htmls/raw/raw_{i}.html')
        logger.info(f"Saved HTML for {key}")
    except Exception as e:
        logger.error(f"Error processing {key}: {e}")

    # Uncomment these lines if needed for further processing
    try:
        html = extract_uu_chapter_html(outer_html)
        xhtml = convert_html_to_xhtml(html)
        raw_data[key] = xhtml
        logger.info(f"Processed HTML for {key}")
    except Exception as e:
        logger.error(f"Error processing HTML for {key}: {e}")

    try:
        with open(raw_json, 'w', encoding='utf-8') as file:
            json.dump(raw_data, file, ensure_ascii=False, indent=4)
        logger.info(f"Raw data written to {raw_json}")
    except Exception as e:
        logger.error(f"Error writing raw data to {raw_json}: {e}")

    logger.info("raw extraction script finished.")

raw_driver.quit()

replace_words = {'’': "'", '“': '"', '”': '"', '—': '-', '…': '...', '‘': "'"}

chapters_data = {}


output_file = f'tk/jsons/chapters_data_{stop_number}.json'

chapters_json = f'tk/jsons/raw/raw_data_{stop_number}.json'
temp_file = f'tk/htmls/temp.html'
temp_file = os.path.abspath(temp_file)

with open(chapters_json, 'r', encoding='utf-8') as file:
    chapters_html = json.load(file)

driver = initiate_driver()
driver.maximize_window()
driver = wait_to_translate(driver)

# chapters_html = slice_dict(chapters_html, 1, 2)

for title, html in chapters_html.items():
    with open(temp_file, 'w', encoding='utf-8') as file:
        file.write(html)
    # temp_file = os.path.abspath(temp_file)
    driver.get(f'file:///{temp_file}')
    relay = True
    exception_count = 0

    while relay:
        exception_count += 1

        driver.refresh()
        time.sleep(2)

        scroll_to_bottom(driver)
        outer_html = copy_full_html(driver)
        html = extract_uu_chapter_html(outer_html)
        html = replace_words_in_html(html, replace_words)
        relay = check_chinese_text(html, exception_count)

        xhtml = convert_html_to_xhtml(html)
        soup = BeautifulSoup(xhtml, 'html.parser')
        with open('tk/htmls/x.html', 'w', encoding='utf-8') as file:
            file.write(soup.prettify())

        if relay:
            scroll_to_top(driver)
        
        chapters_data[title] = xhtml
        print(f"{title} done.")

        # Write chapters_data to f'tk/jsons/chapters_data{x}.json'
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(chapters_data, file, ensure_ascii=False, indent=4)
            

driver.quit()


# for i in range(start_number, stop_number+1):
#     url = f'https://m.uuks.org/b/57664/72080{i}.html'
#     key = f"Chapter {i}"
#     pyperclip.copy(url)
#     # print(url)

#     paste_and_enter()
#     time.sleep(2)

#     scroll_down()


#     while True:
#         page_source = copy_outer_html()

#         if page_source == '':
#             refresh_page()
#             pyautogui.hotkey('ctrl', 'l')
#             pyautogui.press('enter')
#             continue

#         if page_source.startswith('http'):
#             print(page_source)
#             print("The input looks more like a URL than markup.")
#             pyautogui.hotkey('ctrl', 'l')
#             pyautogui.press('enter')
#             # refresh_page()
#             time.sleep(2)
#             continue
        
#         soup = BeautifulSoup(page_source, "html.parser")
#         body_tag = soup.find('div', id='bookContent')


#         if body_tag:
#             contains_chinese, chinese_chars = contains_simplified_chinese(body_tag.text)
#             if contains_chinese:
#                 print("The page contains Simplified Chinese characters:", ''.join(chinese_chars))
#                 refresh_page()
#                 time.sleep(2)
#                 pyautogui.hotkey('ctrl', 'l')
#                 pyautogui.press('enter')
#                 scroll_down()
#                 time.sleep(2)
#                 continue
        
        
#         if soup.find('html').get('lang') == 'en':
#             break

#         refresh_page()


#     copy_outer_html()

#     page_source = pyperclip.paste()
#     soup = BeautifulSoup(page_source, "html.parser")
#     html = extract_uu_chapter_html(soup.prettify())
#     html = replace_words_in_html(html, replace_words)
#     xhtml = convert_html_to_xhtml(html)
#     chapters_data[key] = xhtml
#     print(f"{key} done.")


# # Write chapters_data to f'tk/jsons/chapters_data{x}.json'
#     with open(output_file, 'w', encoding='utf-8') as file:
#            json.dump(chapters_data, file, ensure_ascii=False, indent=4)

# next_tab()

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

