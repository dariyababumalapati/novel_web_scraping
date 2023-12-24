from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

def txt_to_epub(file_to_convert):
    try:
        driver = webdriver.Firefox()
        driver.get("https://convertio.co/txt-epub/")

        label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[@for='pc-upload-add']"))
        )

        driver.execute_script("arguments[0].click();", label)
        time.sleep(2)

        pyautogui.typewrite(file_to_convert)
        time.sleep(2)

        pyautogui.press('right')
        time.sleep(2)

        pyautogui.press('enter')
        time.sleep(2)

        convert_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
        )

        convert_button.click()
        time.sleep(5)

        download_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-blue"))
        )

        download_button.click()
        time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    file_to_convert = r"G:\Projects\Python_projects\novel_web_scraping\text_files\chapters_cleaned\1109-1113_cleaned.txt"
    txt_to_epub(file_to_convert)
