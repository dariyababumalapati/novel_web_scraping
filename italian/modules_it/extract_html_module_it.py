from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

from bs4 import BeautifulSoup

from modules_it.database_module_it import create_connection, set_column_by_id

def initiate_driver(url: str):
    """Initialize a Chrome WebDriver and navigate to the provided URL.

    Args:
        url (str): The URL to navigate to.

    Returns:
        WebDriver: The initialized Chrome WebDriver instance.
    """
    try:
        chrome_options = webdriver.ChromeOptions()
        prefs = {
            "translate_whitelists": {"fr": "en", "zh-CN": "en"},
            "translate": {"enabled": "true"}
        }
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("user-agent=YourCustomUserAgent")
        driver = webdriver.Chrome(options=chrome_options)

        driver.get(url)
        driver.maximize_window()
        print('driver initiated.')

        return driver

    except Exception as e:
        print(f"Error occurred while initializing the driver: {e}")
        return None  # Return None if there's an error initializing the driver


def wait_to_translate(driver):
    """Wait for the page to finish translation before proceeding.

    Args:
        driver (WebDriver): The WebDriver instance.

    Returns:
        WebDriver: The WebDriver instance after the translation is completed.
    """
    try:
        while driver.find_element(By.TAG_NAME, 'html').get_attribute('class') != "translated-ltr":

            driver.refresh()
            time.sleep(3)

        print('Successfully translated.')
        return driver

    except Exception as e:
        print(f"Error occurred while waiting for translation: {e}")
        return None  # Return None if there's an error waiting for translation

def extraction_and_storing(driver, records: list, connection):

    for record in records:
        
        url = record[2]
        driver.get(url)
        id = record[0]
        
        try:
            content_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "w_main")))

            # print(content_element)

            time.sleep(2)

            html_content = content_element.get_attribute('outerHTML')
            # print(html_content)

            set_column_by_id(connection, html_content, id)

        except:
                print(f'missing {record[0]}')

def scroll_to_bottom(driver, pause_time=0.5):
    time.sleep(1)
    # Get scroll height
    total_height = driver.execute_script("return document.body.scrollHeight")
    scroll_stroke = total_height/10

    relay = 0

    while True:
        relay += 1        

        if relay == 10:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")     
            break

        driver.execute_script(f"window.scrollBy(0, {scroll_stroke});")

        time.sleep(pause_time)

def extract_urls(filepath: str):

    connection = create_connection('ree')
    cursor = connection.cursor() 
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    specific_ul = soup.find('ul', id='chapterList')
    print(len(specific_ul))
    chapters = []

    for li in specific_ul.find_all('li')[::-1]:
    
        try:
            chapter_title = li.a.get_text(strip=True)
            
            url_part = li.a.get('href')
            url = f"https://www.uukanshu.net/{url_part}"

            chapters.append((chapter_title, url))
        except:
            print('invalid li element')

    for chapter in chapters:

        # print(chapter_title)
        cursor.execute("""
            INSERT INTO ree_urls (chapter_title, url) VALUES (%s, %s)       
        """, chapter
        )

    connection.commit()
    cursor.close()
    connection.close()

def copy_useful_html(driver):

   try:
    # Wait for the element to be visible and then find the element
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'w_main')))

        time.sleep(1)
    # Get the HTML content of the element
        html_content = element.get_attribute("outerHTML")
        # print(html_content)

        return html_content
   
   except Exception as e:
        print(f"An error in copy_useful_html occurred: {e}")

# confine to the database 


if __name__ == '__main__':
    print('extract_html_module.py running in main.')

