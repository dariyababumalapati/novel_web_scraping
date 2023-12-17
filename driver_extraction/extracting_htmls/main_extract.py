from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import pyautogui

from variab import VariablesCall

from extracting_modules import initiate_driver, click_consent_button, wait_to_translate, copy_useful_html, scroll_to_bottom
from beautifulsoup_editing_modules import remove_elements,remove_elements_with_certain_texts, replace_words_in_html, replace_dots_with_dash, get_chapter_number, create_html_file
from html_files_to_xhtml_lxml import convert_html_to_xhtml, delete_files_in_folder

# url = "https://www.69shuba.com/txt/30539/24457324#google_vignette"
url = "https://www.69shuba.com/txt/10019535/115330344"

driver = initiate_driver(url=url)

click_consent_button(driver)

pyautogui.press('esc')


driver = wait_to_translate(driver, url=url)

cycles = 20

texts_to_remove_list = VariablesCall.texts_to_remove
replace_words_dict = VariablesCall.replace_words
            
output_folder_temp = 'files/xhtml_files_temp/mhag'
delete_files_in_folder(output_folder_temp)

for _ in range(cycles):
    try:
    # Wait for the element to be visible and then find the element
        h1_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "hide720")))

    # Check if the element's text content contains "Chapter"
        if "Chapter" in h1_element.text:
            print("Element contains 'Chapter' in its text content")
            scroll_to_bottom(driver)

            html_content = copy_useful_html(driver=driver)
            soup = remove_elements(html_content)
            soup = remove_elements_with_certain_texts(soup, texts_to_remove=texts_to_remove_list)
            soup = replace_words_in_html(soup, replace_words=replace_words_dict)
            soup = replace_dots_with_dash(soup)
            chapter_number = get_chapter_number(soup=soup)

            file_path = f'files/html_files/mhag/chapter_{chapter_number}.html'
            create_html_file(soup=soup, file_path=file_path)

            
            input_file_path = file_path
            output_file_path = f'files/xhtml_files/mhag/chapter_{chapter_number}.html'
            output_file_path_temp = f'files/xhtml_files_temp/mhag/chapter_{chapter_number}.html'

            convert_html_to_xhtml(input_file_path, output_file_path, output_file_path_temp)

        else:
            print("Element does not contain 'Chapter' in its text content")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        pyautogui.hotkey('shift', 'right')


