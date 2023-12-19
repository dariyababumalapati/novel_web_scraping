from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time

import pyautogui


def initiate_driver(url):
    chrome_options = webdriver.ChromeOptions()
    prefs = {
    "translate_whitelists": {"fr":"en", "zh-CN":"en"},
    "translate":{"enabled":"true"}
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("user-agent=YourCustomUserAgent")
    driver = webdriver.Chrome(options=chrome_options)


    driver.get("https://www.google.com/")


    # # Navigate to a specific URL in the new tab

    driver.switch_to.new_window('tab')

    driver.get(url)

    return driver

def click_consent_button(driver):
    try:

        button_locator = (By.XPATH, '//button[@class="fc-button fc-cta-consent fc-primary-button"]')

        # Wait until the button is clickable
        wait = WebDriverWait(driver, 10) # wait up to 10 seconds
        consent_button = wait.until(EC.element_to_be_clickable(button_locator))

        # Click the button
        consent_button.click()
    except:
        pass

def wait_to_translate(driver, url):
    while driver.find_element(By.TAG_NAME, 'html').get_attribute('class') != "translated-ltr":
        pyautogui.hotkey('shift', 'right')

        time.sleep(5)   

    driver.get(url)

    return driver


def copy_useful_html(driver):

   try:
       # Wait for the element to be visible and then find the element
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'txtnav')))

        time.sleep(3)
       # Get the HTML content of the element
        html_content = element.get_attribute("outerHTML")
        # print(html_content)

        return html_content
   
   except Exception as e:
        print(f"An error occurred: {e}")

def scroll_to_bottom(driver, pause_time=0.5):
   # Get scroll height
   last_height = driver.execute_script("return document.body.scrollHeight")

   while True:
       # Scroll down to bottom
       driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

       # Wait to load page
       time.sleep(pause_time)

       # Calculate new scroll height and compare with last scroll height
       new_height = driver.execute_script("return document.body.scrollHeight")
       if new_height == last_height:
           break
       last_height = new_height


if __name__ == "__main__":
    print("extracting_modules.py is running in main.")