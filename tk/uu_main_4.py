import json
import pyperclip
import time
import os
import sys
import logging
from datetime import datetime
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Add the root directory to the system path
root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_directory)

from logging_config import setup_logging
from utils import save_html

# Logging configuration
setup_logging()
logger = logging.getLogger(__name__)

start_number = 477
stop_number = 525

replace_words = {'’': "'", '“': '"', '”': '"', '—': '-', '…': '...', '‘': "'"}

chapters_data = {}

raw_json = f'tk/jsons/raw/raw_data_{stop_number}.json'

raw_data = {}

primary_url = 'https://m.uuks.org/b/57664/72080526.html'

logger.info("Starting the script.")

def initiate_driver():
    # chrome_options = Options()
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--blink-settings=imagesEnabled=false")
    chrome_options.add_argument("--disable-javascript")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(30)
    return driver

try:
    driver = initiate_driver()
    driver.get(primary_url)
    driver.maximize_window()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "html"))
    )
    logger.info(f"Driver initialized and navigated to {primary_url}")
except Exception as e:
    logger.error(f"Error initializing driver or navigating to primary URL: {e}")
    raise

def fetch_html(driver, url):
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "html"))
        )
        logger.info(f"Navigated to {url}")
        return driver.page_source
    except Exception as e:
        logger.error(f"Error fetching URL {url}: {e}")
        return None

for i in range(start_number, stop_number+1):
    url = f'https://m.uuks.org/b/57664/72080{i}.html'
    key = f"Chapter {i}"

    outer_html = fetch_html(driver, url)
    if outer_html:
        save_html(outer_html, f'tk/htmls/raw_{i}.html')
        logger.info(f"Saved HTML for {key}")

    # Uncomment these lines if needed for further processing
    # try:
    #     html = extract_uu_chapter_html(outer_html)
    #     xhtml = convert_html_to_xhtml(html)
    #     raw_data[key] = xhtml
    #     logger.info(f"Processed HTML for {key}")
    # except Exception as e:
    #     logger.error(f"Error processing HTML for {key}: {e}")

    # try:
    #     with open(raw_json, 'w', encoding='utf-8') as file:
    #         json.dump(raw_data, file, ensure_ascii=False, indent=4)
    #     logger.info(f"Raw data written to {raw_json}")
    # except Exception as e:
    #     logger.error(f"Error writing raw data to {raw_json}: {e}")

driver.quit()
logger.info("Script finished.")
