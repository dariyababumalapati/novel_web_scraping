from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

from extracting_modules import initiate_driver, click_consent_button, wait_to_translate, copy_useful_html, call_the_latest_chapter_url, store_the_chapters_range, store_the_latest_chapter_url, missing_chapter_numbers


from database_module_kgm import create_connection, get_records, get_cn_records



connection = create_connection('kgm')

query_all = "SELECT * FROM kgm_urls;"

records_all = get_records(connection, query_all)

url_all = [r[2] for r in records_all]

url = url_all[0]

driver = initiate_driver(url=url)

driver = wait_to_translate(driver, url=url)



while True:

    cn_li = get_cn_records(connection)

    if not cn_li:
        break

    for id in cn_li:
        index = id-1
        url = url_all[index]
        driver.get(url)

        main_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "w_main")))

        if main_element:
            