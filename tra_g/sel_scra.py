from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

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
            "translate": {"enabled": "true"},
        }
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument(f"user-agent={user_agent}")
        chrome_options.add_argument("user-agent=YourCustomUserAgent")
        chrome_options.add_argument("start-maximized")

        driver = webdriver.Chrome(options=chrome_options)

        driver.get(url)
        print("driver initiated.")

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
        while (
            driver.find_element(By.TAG_NAME, "html").get_attribute("class")
            != "translated-ltr"
        ):
            driver.refresh()
            time.sleep(3)

        print("Successfully translated.")
        return driver

    except Exception as e:
        print(f"Error occurred while waiting for translation: {e}")
        return None  # Return None if there's an error waiting for translation

url = "https://www.uuks.org/b/53573/669662.html"
translated_url = f"https://translate.google.com/translate?sl=auto&tl=es&u={url}"

driver = initiate_driver(translated_url)

# Wait for the page to finish translation
wait_to_translate(driver)

driver.implicitly_wait(10)

page_source = driver.page_source

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Save the soup to an HTML file
with open("tra_g/htmls/output4.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())

# print("HTML content saved to output2.html")

driver.quit()