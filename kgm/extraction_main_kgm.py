from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from extract_html_module_kgm import initiate_driver, wait_to_translate, copy_useful_html

from database_module_kgm import create_connection, get_records, get_cn_records_id, set_column_by_id

import time

query_all = "SELECT * FROM kgm_urls;"
records_all = get_cn_records_id(query_all)
url_all = [r[2] for r in records_all]

url = url_all[0]


# ex
# print(url)
# cn_li = get_cn_records()
# print(cn_li)


driver = initiate_driver(url=url)

driver = wait_to_translate(driver, url=url)



while True:

    cn_li = get_cn_records_id()()

    if not cn_li:
        break

    for id in cn_li:

        index = id-1
        url = url_all[index]
        print(url)
        driver.get(url)

        html_content = copy_useful_html(driver)
        content_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'contentbox')))
        content_box_content = content_box.get_attribute('outerHTML')
        
        set_column_by_id('raw_html', html_content, id)    











            