from driver_setup_module import DriverSetup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import json

from helper_functions import save_json


class BookBar:
    def __init__(self, url):
        driver_object = DriverSetup(url)
        self.driver = driver_object.driver
    
    def get_title_and_urls(self):
        """
        Extracts titles and URLs of chapters from a webpage.

        Args:
        driver (webdriver): The Selenium WebDriver.

        Returns:
        dict: A dictionary of chapter titles and their corresponding URLs.
        """
        chapters_dictionary = {}
        
        try:

            # Wait for the catalog element to be present before proceeding
            catalog = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'catalog'))
            )

            if catalog:
                print('Catalog exists')
                
                self.scroll_to_bottom()

                chapters_index = catalog.find_element(By.TAG_NAME, 'ul')
                chapters_list = chapters_index.find_elements(By.TAG_NAME, 'li')

                for chapter in chapters_list:
                    chapter_link = chapter.find_element(By.TAG_NAME, 'a')
                    chapter_title = chapter_link.text.strip()  # strip() to remove any leading/trailing whitespace
                    chapter_url = chapter_link.get_attribute('href')

                    chapters_dictionary[chapter_title] = chapter_url

        except Exception as e:
            print("An error occurred:", e)
            # Optionally, you could re-raise the exception or handle it in another way
            # raise

        return chapters_dictionary
    
    def scroll_to_bottom(self, pause_time=1):
        time.sleep(1)
        # Get scroll height
        total_height = self.driver.execute_script("return document.body.scrollHeight")
        scroll_stroke = total_height/10

        relay = 0

        while True:
            relay += 1        

            if relay == 10:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")     
                break

            self.driver.execute_script(f"window.scrollBy(0, {scroll_stroke});")

            time.sleep(pause_time)

if __name__ == '__main__':

    url = 'https://www.69shu.pro/book/55016/'

    file_path = 'book_bar/c_t.json'

    ming_dict_file_path = 'book_bar/ming_dict_raw.json'

    bookb = BookBar(url)
    
    replace_words_dict = {'’' : "'", '”' : "'", '“' : "'",}
    
    ming_dict = bookb.get_title_and_urls()

    save_json(ming_dict_file_path, ming_dict)
    # temp_dict = ming_dict.copy()
    
    # new_ming_dict = {}
    
    # for key, value in temp_dict.items():
    #     new_key = key
    #     for old_char, new_char in replace_words_dict.items():
    #         new_key = new_key.replace(old_char, new_char)

    #     new_ming_dict[new_key] = value

    # ming_dict = new_ming_dict

    # with open (file_path, 'w', encoding='utf-8') as f:
    #     json.dump(ming_dict, f, indent=4)
