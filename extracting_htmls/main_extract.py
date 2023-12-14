from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

import time

import pyautogui

from extracting_htmls.extracting_modules import click_consent_button, initiate_driver, wait_to_translate


url = "https://www.69shuba.com/txt/30539/24457324#google_vignette"

driver = initiate_driver(url=url)

click_consent_button(driver)

pyautogui.press('esc')


driver = wait_to_translate(driver, url=url)

cycles = 10

for _ in range(cycles):
    try:
    # Wait for the element to be visible and then find the element
        h1_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "hide720")))

    # Check if the element's text content contains "Chapter"
        if "Chapter" in h1_element.text:
            print("Element contains 'Chapter' in its text content")

        else:
            pyautogui.hotkey('shift', 'right')
            print("Element does not contain 'Chapter' in its text content")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        #  time.sleep(50)
        driver.quit()




# ele = driver.find_element(By.CLASS_NAME, 'txtnav')

# ele_html = ele.get_attribute('outerHTML')
# print("HTML content of the 'ele' element:")
# print(ele_html)

# with open('sample_html.html', 'w', encoding='utf-8') as file:
#     file.write(ele_html)

# pyautogui.press('esc')

# time.sleep(300)


# h1_element = soup.find('h1', class_='hide720')

# # Check if the h1 element exists and contains 'Chapter' in its text
# if h1_element and 'Chapter' in h1_element.get_text():
#     try:
#         # Wait for the element to be visible and then find the element
#         element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//font[contains(text(), 'next chapter')]")))

#         # Click the element
#         element.click()
#     except NoSuchElementException:
#         print("Element not found")
#     finally:
#     # Close the browser
#         driver.quit()