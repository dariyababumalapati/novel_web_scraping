from selenium import webdriver
import time

from extract_html_module_kgm import initiate_driver, wait_to_translate, scroll_to_bottom

# Your WebDriver setup
driver = webdriver.Chrome()  # Or any other WebDriver you're using
url = "https://www.uukanshu.net/b/43112/94187.html#gsc.tab=0"

driver = initiate_driver(url)

# driver = wait_to_translate(driver)

scroll_to_bottom(driver)


print('ok')
# scroll_position = driver.execute_script("return window.scrollY;")
# print(f"Current scroll position: {scroll_position}")


# total_height = driver.execute_script("return document.body.scrollHeight")
# print(f"Total scroll height: {total_height}")


# time.sleep(500)

