from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time


import pyautogui

chrome_options = webdriver.ChromeOptions()
prefs = {
 "translate_whitelists": {"fr":"en", "zh-CN":"en"},
 "translate":{"enabled":"true"}
}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://www.google.com/")


# # Navigate to a specific URL in the new tab

driver.switch_to.new_window('tab')

url = "https://www.69shuba.com/txt/30539/24457324#google_vignette"
driver.get(url)

button_locator = (By.XPATH, '//button[@class="fc-button fc-cta-consent fc-primary-button"]')

# Wait until the button is clickable
wait = WebDriverWait(driver, 10) # wait up to 10 seconds
button = wait.until(EC.element_to_be_clickable(button_locator))

# Click the button
button.click()


pyautogui.press('esc')


while driver.find_element(By.TAG_NAME, 'html').get_attribute('class') != "translated-ltr":
    pyautogui.hotkey('shift', 'right')

    time.sleep(5)

url = "https://www.69shuba.com/txt/30539/24457324#google_vignette"
driver.get(url)


pyautogui.press('esc')

time.sleep(300)


