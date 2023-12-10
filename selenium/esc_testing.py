from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()

url_li = ["https://www.google.com/", "https://www.69shuba.com/txt/30539/24457324#google_vignette"]

driver.get(url_li[0])

# button = driver.find_element(By.CLASS_NAME, "QS5gu sy4vM")
wait = WebDriverWait(driver, 10)

# button = wait.until(EC.element_to_be_clickable(By.CLASS_NAME, "QS5gu sy4vM" ))
# button.click()

# actions = ActionChains(driver)

# actions.key_down(Keys.CONTROL).send_keys('l').key_up(Keys.CONTROL).perform()
# actions.send_keys(Keys.ESCAPE).perform()

time.sleep(300)