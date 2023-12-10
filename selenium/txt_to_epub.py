from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import pyautogui

# Path to ChromeDriver - Change this to your own path

# File path to be converted
file_to_convert = r"G:\Projects\Python_projects\novel_web_scraping\selenium\web_testing_file.txt"


# Initialize Chrome driver
driver = webdriver.Firefox()

# Open the website
driver.get("https://convertio.co/txt-epub/")


try:
        # Find the label element
    label = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//label[@for='pc-upload-add']"))
    )

    # Click on the label element using JavaScript
    driver.execute_script("arguments[0].click();", label)
    time.sleep(2)

    pyautogui.typewrite(file_to_convert)
    time.sleep(2)

    pyautogui.press('enter')
    time.sleep(2)

    pyautogui.press('enter')
    time.sleep(2)


    convert_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
    )

# Click on the 'Convert' button
    convert_button.click()
    time.sleep(5)

#     driver.execute_script("""
#    var downloadButton = document.querySelector('.dt-btn .btn');
#    setTimeout(function() {
#        downloadButton.click();
#    }, 10000); // Adjust delay as needed
#    """)

    download_button = WebDriverWait(driver, 10).until(
      EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-blue"))
  )

  # Click on the 'Download' button
    download_button.click()

    time.sleep(5)

    # Find the 'Choose Files' input element
    # choose_files_input = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "pc-upload-add"))
    # )

    # # Send the file path to the 'Choose Files' input
    # file_to_convert = "G:/Projects/Python_projects/novel_web_scraping/selenium/driver_testing.txt"
    # choose_files_input.click()
    # # choose_files_input.send_keys(file_to_convert)

    # You may need to add further steps to initiate the conversion process or wait for it to start

except Exception as e:
    print(f"An error occurred: {str(e)}")

time.sleep(5)  # Wait for 30 seconds

# try:
#     # Find and click 'Choose files' button
#     choose_files_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//input[@type='file']"))
#     )
#     choose_files_button.send_keys(file_to_convert)

#     # Find and click 'Convert' button
#     convert_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Convert')]"))
#     )
#     convert_button.click()

#     # Wait for the conversion to complete (adjust the time based on actual conversion time)
#     time.sleep(30)  # Wait for 30 seconds

#     # Find and click the download link
#     download_link = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, "//a[@class='download btn btn-default btn-primary']"))
#     )
#     download_link.click()

# except Exception as e:
#     print(f"An error occurred: {str(e)}")

# finally:
#     driver.quit()  # Close the browser session

"sub-label-text"