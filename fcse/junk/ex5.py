import time
import pyperclip
import re

def contains_chinese(text):
    # Define a regex pattern that matches Chinese characters
    chinese_pattern = re.compile('[\u4e00-\u9fff]')
    # Search for Chinese characters in the text
    if chinese_pattern.search(text):
        return True
    return False

while True:
    time.sleep(3)
    # process_page()  # Assuming this is defined elsewhere
    chapter_content = pyperclip.paste()
    if contains_chinese(chapter_content):
        print("Chinese text detected in the chapter content.")
    else:
        print("No Chinese text detected in the chapter content.")
