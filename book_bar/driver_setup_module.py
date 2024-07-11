from selenium import webdriver
from selenium.webdriver.common.by import By

import time

class DriverSetup:
    def __init__(self, url):
        self.url = url
        self.driver = self.initiate_driver()
        self.driver = self.wait_to_translate()

    def initiate_driver(self):
        """Initialize a Chrome WebDriver and navigate to the provided URL.

        Returns:
            WebDriver: The initialized Chrome WebDriver instance, or None if an error occurs.
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

            driver.get(self.url)
            driver.maximize_window()
            print('Driver initiated.')

            return driver

        except Exception as e:
            print(f"Error occurred while initializing the driver: {e}")
            return None  # Return None if there's an error initializing the driver


    def wait_to_translate(self):
        """Wait for the page to finish translation before proceeding.

        Args:
            driver (WebDriver): The WebDriver instance.

        Returns:
            WebDriver: The WebDriver instance after the translation is completed.
        """
        try:
            while self.driver.find_element(By.TAG_NAME, 'html').get_attribute('class') != "translated-ltr":

                self.driver.refresh()
                time.sleep(3)

            print('Successfully translated.')
            return self.driver

        except Exception as e:
            print(f"Error occurred while waiting for translation: {e}")
            return None  # Return None if there's an error waiting for translation

# Example of using the class
if __name__ == "__main__":
    url = "https://www.69shu.pro/book/55016/"
    setup = DriverSetup(url)
    if setup.driver:
        print("Driver is ready for use.")
    else:
        print("Failed to initialize the driver.")
