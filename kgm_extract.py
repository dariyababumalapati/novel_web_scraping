from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import re 

import pyautogui

from variab import VariablesCall

from database_actions_module.db_initiator import create_connection

from extracting_modules import initiate_driver, wait_to_translate, scroll_to_bottom, copy_useful_html
# from driverextracting_modules import initiate_driver, click_consent_button, wait_to_translate, copy_useful_html, call_the_latest_chapter_url, store_the_chapters_range, store_the_latest_chapter_url, missing_chapter_numbers
from beautifulsoup_editing_modules import replace_words_in_html, replace_dots_with_dash, create_html_file
from driver_extraction.extracting_htmls.html_files_to_xhtml_lxml import convert_html_to_xhtml, delete_files_in_folder


# data_base = 'novel_web_scraping'
# connection = create_connection(data_base)
# cursor = connection.cursor()

# cursor.execute('''SELECT url from kgm LIMIT 1;''')

# url = cursor.fetchone()[0]
url = ' https://www.uukanshu.net//b/43112/59751.html'


driver = initiate_driver(url)


time.sleep(10)


driver = wait_to_translate(driver, url=url)

cycles = 45

replace_words_dict = VariablesCall.replace_words
            
output_folder_temp = 'files/xhtml_files_temp/mhag'
delete_files_in_folder(output_folder_temp)

chapters_list = []
chapter_number = 82

incomplete_load_flag = False

for c in range(cycles):

    try:
        # Wait for the element to be visible and then find the element
        h1_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "timu")))
        chapter_number += 1

#         # end_chapter_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(By.XPATH, "//*[contains(text()='End of this chapter')]"))

#     # Check if the element's text content contains "Chapter"
        if "Chapter" in h1_element.text:
            print("Element contains 'Chapter' in its text content")
            scroll_to_bottom(driver)

            html_content = copy_useful_html(driver=driver)
            soup = replace_words_in_html(soup, replace_words=replace_words_dict)
            soup = replace_dots_with_dash(soup)

            chapters_list.append(int(chapter_number))

            file_path = f'files/html_files/kgm/chapter_{chapter_number}.html'
            create_html_file(soup=soup, file_path=file_path)

            input_file_path = file_path
            output_file_path = f'files/xhtml_files/kgm/chapter_{chapter_number}.html'
            output_file_path_temp = f'files/xhtml_files_temp/kgm/chapter_{chapter_number}.html'

            convert_html_to_xhtml(input_file_path, output_file_path, output_file_path_temp)

            pyautogui.hotkey('shift', 'right')


        elif not incomplete_load_flag:
            incomplete_load_flag = True
            driver.refresh()
            time.sleep(3)
            
        else:
            print("Element does not contain 'Chapter' in its text content")
            
            # missing_chapters(chapters_list=chapters_list)

            incomplete_load_flag = False

            pyautogui.hotkey('shift', 'right')

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        time.sleep(1)

# store_the_latest_chapter_url(driver=driver)
# store_the_chapters_range(chapters_list=chapters_list)
# # missing_chapter_numbers(chapters_list)