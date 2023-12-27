import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time


def initiate_driver(url: str):
    chrome_options = webdriver.ChromeOptions()
    prefs = {
    "translate_whitelists": {"fr":"en", "zh-CN":"en"},
    "translate":{"enabled":"true"}
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("user-agent=YourCustomUserAgent")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)

    return driver

def click_consent_button(driver):
    try:

        button_locator = (By.XPATH, '//button[@class="fc-button fc-cta-consent fc-primary-button"]')

        # Wait until the button is clickable
        wait = WebDriverWait(driver, 5) # wait up to 10 seconds
        consent_button = wait.until(EC.element_to_be_clickable(button_locator))

        # Click the button
        consent_button.click()
    except:
        pass

def click_next_chapter_chinese(driver):

    end_chapter_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='下一章']")))
    end_chapter_element.click()
    
def click_next_chapter_english(driver):
    end_chapter_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='next chapter']")))
    print(end_chapter_element)

def wait_to_translate(driver, url):
    while driver.find_element(By.TAG_NAME, 'html').get_attribute('class') != "translated-ltr":
        click_next_chapter_chinese(driver=driver)
        time.sleep(3)

    driver.get(url)

    return driver

def copy_useful_html(driver):

   try:
       # Wait for the element to be visible and then find the element
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, '')))

        time.sleep(3)
       # Get the HTML content of the element
        html_content = element.get_attribute("outerHTML")
        # print(html_content)

        return html_content
   
   except Exception as e:
        print(f"An error in copy_useful_html occurred: {e}")



if __name__ == '__main__':
    print('extract_html_module.py running in main.')