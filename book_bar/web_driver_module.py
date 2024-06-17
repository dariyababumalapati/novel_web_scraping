from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time


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

def get_title_and_urls(driver):
    """
    Extracts titles and URLs of chapters from a webpage.

    Args:
    driver (webdriver): The Selenium WebDriver.

    Returns:
    dict: A dictionary of chapter titles and their corresponding URLs.
    """
    
    chapters_dictionary = {}
    
    try:
        # Assuming wait_to_translate is an adequately defined function
        wait_to_translate(driver)

        # Wait for the catalog element to be present before proceeding
        catalog = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'catalog'))
        )

        if catalog:
            print('Catalog exists')

            chapters_index = catalog.find_element(By.TAG_NAME, 'ul')
            chapters_list = chapters_index.find_elements(By.TAG_NAME, 'li')

            for chapter in chapters_list[:20]:
                chapter_link = chapter.find_element(By.TAG_NAME, 'a')
                chapter_title = chapter_link.text.strip()  # strip() to remove any leading/trailing whitespace
                chapter_url = chapter_link.get_attribute('href')
                chapters_dictionary[chapter_title] = chapter_url

    except Exception as e:
        print("An error occurred:", e)
        # Optionally, you could re-raise the exception or handle it in another way
        # raise

    return chapters_dictionary


if __name__ == '__main__':
    print('web_driver_module.py running in main.')

    url = 'https://www.69shu.pro/book/55016/'

    driver = initiate_driver(url)
 
    # wait_to_translate(driver)

    # catalog = driver.find_element(By.ID, 'catalog')

    # if catalog:
    #     print('it exists')


    # chapters_index = catalog.find_element(By.TAG_NAME, 'ul')


    # chapters_list = chapters_index.find_elements(By.TAG_NAME, 'li')

    # for chapter in chapters_list[:20]:
    #     chapter_link = chapter.find_element(By.TAG_NAME, 'a')  # Proper way to find the 'a' tag
    #     print(chapter_link.text)  # Print the text of the 'a' tag

#     print(chapters_list)

