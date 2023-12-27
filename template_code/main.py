from selenium import webdriver

import time

from extract_html_module import initiate_driver, wait_to_translate


url = 'https://www.69shuba.com/txt/10019535/115324030'

driver = initiate_driver(url)



driver = wait_to_translate(driver, url)

driver.get('https://www.uukanshu.net/b/43112/102881.html#gsc.tab=0')

time.sleep(100)

