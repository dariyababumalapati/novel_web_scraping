from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import pyautogui

from variab import VariablesCall

from other.extracting_modules import initiate_driver, click_consent_button, wait_to_translate, copy_useful_html, scroll_to_bottom, click_next_chapter_english
from other.beautifulsoup_editing_modules import parse_the_html, get_chapter_number, create_html_file
# from html_files_to_xhtml_lxml import convert_html_to_xhtml, delete_files_in_folder

# url = "https://www.69shuba.com/txt/30539/24457324#google_vignette"
url = "https://www.69shuba.com/txt/10019535/115331694"

driver = initiate_driver(url=url)

click_consent_button(driver)

driver = wait_to_translate(driver, url=url)

cycles = 10

for c in range(cycles):

    try:
    # Wait for the element to be visible and then find the element
        h1_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "hide720")))
        # end_chapter_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(By.XPATH, "//*[contains(text()='End of this chapter')]"))

    # Check if the element's text content contains "Chapter"
        if "Chapter" in h1_element.text:
            print("Element contains 'Chapter' in its text content")
            scroll_to_bottom(driver)


            html_content = copy_useful_html(driver=driver)
            soup = parse_the_html(html_content=html_content)
            chapter_number = get_chapter_number(soup=soup)

            file_path = f'G:/Projects/Python_projects/project_files/files_novel_web_scraping/html_files/hegemon_of_ancient_mediterranean/raw_html_files/chapter_{chapter_number}_raw.html'
            create_html_file(soup=soup, file_path=file_path)

            print(chapter_number)

        else:
            print("Element does not contain 'Chapter' in its text content")
            # driver.refresh()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        pyautogui.hotkey('shift', 'right')
        time.sleep(0.5)

