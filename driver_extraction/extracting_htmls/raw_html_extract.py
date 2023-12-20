from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import pyautogui

# from variab import VariablesCall

from extracting_modules import initiate_driver, click_consent_button, wait_to_translate, copy_useful_html, scroll_to_bottom, click_next_chapter_english, store_the_latest_chapter_url, call_the_latest_chapter_url
from beautifulsoup_editing_modules import get_chapter_number, create_html_file


url = "https://www.69shuba.com/txt/10019535/115331336"

driver = initiate_driver(url=url)

click_consent_button(driver)

# pyautogui.press('esc')


driver = wait_to_translate(driver, url=url)

cycles = 5

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

            chapter_number = get_chapter_number(html_content)

            file_path = f"G:/Projects/Python_projects/project_files/files_novel_web_scraping/html_files/raw_html_files/raw_chapter_{chapter_number:04}.html"
            create_html_file(soup=html_content, file_path=file_path)

            # click_next_chapter_english(driver=driver)

            if c == cycles-1:
                store_the_latest_chapter_url(driver)

        else:
            print("Element does not contain 'Chapter' in its text content")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        pyautogui.hotkey('shift', 'right')

        time.sleep(1)

driver.quit()