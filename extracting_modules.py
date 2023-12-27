import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time


def initiate_driver(url):
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
    # next_chapter_link = WebDriverWait(driver, 10).until(
    # EC.presence_of_element_located((By.XPATH, "//a[@href and contains(text(), 'next chapter')]"))
    # )

# Click the "Next Chapter" link

    # end_chapter_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='next chapter']")))
    end_chapter_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='next chapter']")))
    print(end_chapter_element)
    # end_chapter_element.click()

def wait_to_translate(driver, url):
    while driver.find_element(By.TAG_NAME, 'html').get_attribute('class') != "translated-ltr":
        click_next_chapter_chinese(driver=driver)
        time.sleep(3)

    driver.get(url)

    return driver


def copy_useful_html(driver):

   try:
       # Wait for the element to be visible and then find the element
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'contentbox')))

        time.sleep(3)
       # Get the HTML content of the element
        html_content = element.get_attribute("outerHTML")
        # print(html_content)

        return html_content
   
   except Exception as e:
        print(f"An error in copy_useful_html occurred: {e}")

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

       time.sleep(pause_time)


def store_the_latest_chapter_url(driver):
    current_url = driver.current_url

    url_dict = {'latest_url': current_url}

    with open('inproject_data.json', 'w', encoding='utf-8') as f:
        json.dump(url_dict, f)

def call_the_latest_chapter_url():
        with open('inproject_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

            url = data['latest_url']

            return url

def store_the_chapters_range(chapters_list:list):

    with open('inproject_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    chapters_range = f'{chapters_list[0]} - {chapters_list[-1]}'
    chapters_range_dict = {'chapters_range': chapters_range}

    data.update(chapters_range_dict)

    with open('inproject_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)

def call_the_chapters_range():
    with open('inproject_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

        chapters_range = data['chapters_range']

        return chapters_range

def missing_chapter(chapters_list:list):
    if chapters_list:
        missing_chapter = chapters_list[-1] + 1
        print(missing_chapter)
    
    else:
        print('first loading chapter is missing.')

def missing_chapter_numbers(numbers_list:list):

    expected_range = range(numbers_list[0], numbers_list[-1] + 1)
    missing_numbers = [num for num in expected_range if num not in numbers_list]

    print("Missing numbers:", missing_numbers)



if __name__ == "__main__":
    print("extracting_modules.py is running in main.")