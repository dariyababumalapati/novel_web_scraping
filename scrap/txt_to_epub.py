from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

from autocopy import get_inproject_data

from share_file.g_drive_upolad import upload_f_to_g_drive


def txt_to_epub(file_to_convert):
    try:
        driver = webdriver.Firefox()
        driver.get("https://convertio.co/txt-epub/")

        label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[@for='pc-upload-add']"))
        )

        driver.execute_script("arguments[0].click();", label)
        time.sleep(5)

        pyautogui.typewrite(file_to_convert)
        time.sleep(5)

        pyautogui.press('right')
        time.sleep(2)

        pyautogui.press('left')
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
    novels = ['ree', 'ra', 'kor', 'nep', 'ming', 'rmf', 'fsce']

    novel = novels[6]

    chapter_number = 50

    d_folder_list = get_inproject_data()[1]

    d_folder = d_folder_list['fcse']

    up_file_path = rf"C:\Users\91833\OneDrive\Desktop\books\{novel}\update\{novel}_{chapter_number}.txt"
    file_name = rf"C:\Users\91833\Downloads\{novel}_{chapter_number}.epub"

    txt_to_epub(up_file_path)

    upload_f_to_g_drive(file_name=file_name, folder_id=d_folder)
