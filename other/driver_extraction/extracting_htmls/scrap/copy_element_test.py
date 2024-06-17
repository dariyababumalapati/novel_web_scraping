from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time



chrome_options = webdriver.ChromeOptions()
prefs = {
"translate_whitelists": {"fr":"en", "zh-CN":"en"},
"translate":{"enabled":"true"}
}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("user-agent=YourCustomUserAgent")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.google.com/")
element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'mngb')))

print(element)
print('ok')

html_content = element.get_attribute("outerHTML")

print(html_content)
time.sleep(300)