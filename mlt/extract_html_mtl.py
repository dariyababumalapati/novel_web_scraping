from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time
import os

def initiate_driver(url="http://www.baidu.com"):
    """Initialize a Chrome WebDriver and navigate to the provided URL.

    Args:
        url (str): The URL to navigate to.

    Returns:
        WebDriver: The initialized Chrome WebDriver instance.
    """
    try:
        chrome_options = uc.ChromeOptions()
        prefs = {
            "translate_whitelists": {"fr": "en", "zh-CN": "en"},
            "translate": {"enabled": "true"},
            "profile.managed_default_content_settings.images": 2,  # Disable images
            "profile.default_content_setting_values.notifications": 2,  # Disable notifications
        }

        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument(f"user-agent={user_agent}")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        print("driver initiated.")

        return driver

    except Exception as e:
        print(f"Error occurred while initializing the driver: {e}")
        return None  # Return None if there's an error initializing the driver

def raw_driver(url):
    """Initialize a Chrome WebDriver and navigate to the provided URL.

    Args:
        url (str): The URL to navigate to.

    Returns:
        WebDriver: The initialized Chrome WebDriver instance.
    """
    try:
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--blink-settings=imagesEnabled=false")
        chrome_options.add_argument("--disable-javascript")
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        chrome_options.add_argument(f"user-agent={user_agent}")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        print("driver initiated.")

        return driver

    except Exception as e:
        print(f"Error occurred while initializing the driver: {e}")
        return None  # Return None if there's an error initializing the driver

def click_consent_button_mid(self):
        try:
            consent_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='fc-button fc-cta-consent fc-primary-button']"))
            )
            consent_button.click()
            print("Clicked the consent button.")
        except Exception as e:
            print(f"Consent button not found or not clickable: {e}")

def click_consent_button(driver):
    try:
        button_locator = (
            By.XPATH,
            '//button[@class="fc-button fc-cta-consent fc-primary-button"]',
        )

        # Wait until the button is clickable
        wait = WebDriverWait(driver, 5)  # wait up to 10 seconds
        consent_button = wait.until(EC.element_to_be_clickable(button_locator))

        # Click the button
        consent_button.click()
        print("Clicked the consent button.")

    except:
        print(f"Consent button not found or not clickable")

        pass

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



def scroll_to_bottom(driver, pause_time=0.5):
    # Get scroll height
    total_height = driver.execute_script("return document.body.scrollHeight")
    scroll_stroke = total_height / 10

    relay = 0

    while relay <= 10:
        relay += 1

        driver.execute_script(f"window.scrollBy(0, {scroll_stroke});")

        time.sleep(pause_time)

def scroll_to_top(driver, pause_time=0.5):
    # Get current scroll position
    current_position = driver.execute_script("return window.pageYOffset")
    scroll_stroke = current_position / 10

    relay = 0

    while relay <= 10:
        relay += 1

        driver.execute_script(f"window.scrollBy(0, {-scroll_stroke});")

        time.sleep(pause_time)


def copy_useful_html(driver):
    try:
        # Wait for the element to be visible and then find the element
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "bookContent"))
        )

        time.sleep(3)
        # Get the HTML content of the element
        html_content = element.get_attribute("outerHTML")
        # print(html_content)

        return html_content

    except Exception as e:
        print(f"An error in copy_useful_html occurred: {e}")

def copy_full_html(driver):
    try:
        # Wait until the page is fully loaded by checking for a specific element
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "html"))
        )

        # Optional: Add sleep if necessary for dynamic content
        time.sleep(1)

        # Get the HTML content of the entire page
        html_content = driver.page_source

        return html_content

    except Exception as e:
        print(f"An error in copy_full_html occurred: {e}")

# confine to the database


if __name__ == "__main__":

    file_path = "tk/htmls/chinese_501.html"
    file_path = os.path.abspath("tk/htmls/chinese_501.html")

    
    # url = "https://m.uuks.org/b/57664/72080102.html"
    driver = raw_driver()
    driver.get(f'file:///{file_path}')
    # driver = raw_driver(f'file:///{file_path}')
    # click_consent_button(driver)
    driver = wait_to_translate(driver)
    scroll_to_bottom(driver)
    scroll_to_top(driver)
    html = copy_full_html(driver)
    driver.quit()
    print("extract_html_module.py running in main.")

    with open("test_full_2.html", "w", encoding="utf-8") as file:
        file.write(html)