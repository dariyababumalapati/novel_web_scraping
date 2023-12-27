from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("chrome://settings/")
# driver.get("https://www.google.com/")
language_button = driver.find_element(By.ID, "element_id")

time.sleep(100000)