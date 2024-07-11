import json
import time
import os
import sys

from extract_html_module_tk import raw_driver, click_consent_button, copy_full_html

from bs4_html_module import extract_uu_chapter_html, convert_html_to_xhtml
from utils import save_html


import logging


# Add the root directory to the system path
root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_directory)

from logging_config import setup_logging



start_number = 475

stop_number = 525


replace_words = {'’': "'", '“': '"', '”': '"', '—': '-', '…': '...', '‘': "'"}

chapters_data = {}

raw_json = f'tk/jsons/raw/raw_data_{stop_number}.json'

raw_data = {}

primary_url = 'https://m.uuks.org/b/57664/72080526.html'

# Initialize logging
setup_logging()
logger = logging.getLogger(__name__)


try:
    raw_driver = raw_driver(primary_url)
    # raw_driver.maximize_window()
    click_consent_button(raw_driver)
    time.sleep(1)
    logger.info(f"Driver initialized and navigated to {primary_url}")
except Exception as e:
    logger.error(f"Error initializing driver or navigating to primary URL: {e}")
    raise

for i in range(start_number, stop_number+1):
    url = f'https://m.uuks.org/b/57664/72080{i}.html'
    key = f"Chapter {i}"

    try:
        raw_driver.get(url)
        logger.info(f"Navigated to {url}")
        outer_html = copy_full_html(raw_driver)
        save_html(outer_html, f'tk/htmls/raw/raw_{i}.html')
        logger.info(f"Saved HTML for {key}")
    except Exception as e:
        logger.error(f"Error processing {key}: {e}")

    # Uncomment these lines if needed for further processing
    try:
        html = extract_uu_chapter_html(outer_html)
        xhtml = convert_html_to_xhtml(html)
        raw_data[key] = xhtml
        logger.info(f"Processed HTML for {key}")
    except Exception as e:
        logger.error(f"Error processing HTML for {key}: {e}")

    try:
        with open(raw_json, 'w', encoding='utf-8') as file:
            json.dump(raw_data, file, ensure_ascii=False, indent=4)
        logger.info(f"Raw data written to {raw_json}")
    except Exception as e:
        logger.error(f"Error writing raw data to {raw_json}: {e}")

    logger.info("Script finished.")

raw_driver.quit()
