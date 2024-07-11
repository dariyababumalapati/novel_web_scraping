import time
from itertools import dropwhile, takewhile
import pyperclip
import json
import re

import pyautogui

from itertools import dropwhile, takewhile

def get_start_end_numbers(start_num, end_num, cycles):
        if start_num and end_num:
            start_number = int(start_num)
            end_number = int(end_num)
            print("Both start_num and end_num provided.")
        else:
            print("Either start_num or end_num is not provided.")
            with open('tk/inproject_data.json', 'r', encoding='utf-8') as f:
                data = json.load(f)

            start_number = data['chapter_number'] + 1
            end_number = start_number + cycles
        
        return start_number, end_number


def working_dictionary(full_dict, start_number, end_number):
    
    start_key = f'Chapter {start_number}'
    end_key = f'Chapter {end_number}'
    print(start_key, end_key)
    # Drop elements until start_key is found
    dropped = dropwhile(lambda item: item[0] != start_key, full_dict.items())

    # Take elements while we haven't reached the end_key
    result = takewhile(lambda item: item[0] != end_key, dropped)

    # Create a dictionary from the resulting items
    work_dict = {key: url for key, url in result}
    
    # Ensure the end_key is included
    if end_key in full_dict:
        work_dict[end_key] = full_dict[end_key]

    return work_dict



def update_chapter_number(end_number, cycles):

    with open('inproject_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    if end_number:
            data['chapter_number'] = end_number
    else:
        data['chapter_number'] = data['chapter_number'] + cycles

    with open('inproject_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def get_inproject_data():
    with open('inproject_data.json', 'r') as f:
        data = json.load(f)
        chapter_number = data['chapter_number']
        d_folder_list = data['d_folder_list']
        novels = data['novels']

        return chapter_number, d_folder_list, novels

def open_chrome():
    # Allow some time to switch to the desktop
    time.sleep(2)

    # Open start menu
    pyautogui.hotkey('win', 'r')

    # Wait for the run dialog to open
    time.sleep(1)

    # Type 'chrome' to search for Chrome
    pyautogui.write('chrome')

    # Press Enter to open Chrome
    pyautogui.press('enter')
    # Wait for Chrome to open
    time.sleep(2)

    # Maximize the window
    # pyautogui.hotkey('win', 'up')

def next_tab():
    pyautogui.hotkey('alt', 'tab')  # Switch to Notepad
    time.sleep(0.5)  # Add a short delay between key presses

def paste_and_enter():
    pyautogui.hotkey('ctrl', 'l')  # Press Ctrl+L
    time.sleep(0.5)  # Add a short delay between key presses
    pyautogui.hotkey('ctrl', 'v')  # Press Ctrl+L
    # time.sleep(0.5)  # Add a short delay between key presses
    # pyautogui.typewrite(url)  # Type the URL
    time.sleep(0.5)  # Add a short delay between key presses
    pyautogui.press('enter')  # Press Enter
    time.sleep(1)  # Add a short delay between key presses


def scroll_down():
    time.sleep(2)  # Add a short delay between key presses
    for _ in range(10):
        pyautogui.scroll(-500)
        time.sleep(0.5)  # Add a short delay between key presses

def copy_outer_html():
    # Open developer tools
    pyautogui.hotkey('ctrl', 'shift', 'i')
    time.sleep(2)  # Wait for developer tools to open

    # Focus on the Elements tab (this might vary depending on the browser)
    pyautogui.hotkey('ctrl', 'shift', 'c')
    time.sleep(1)  # Wait for the focus to switch to Elements

    # Copy the outer HTML of the <html> element
    # This sequence might vary based on the browser and the current state of the developer tools
    pyautogui.hotkey('ctrl', 'a')  # Select all
    pyautogui.hotkey('ctrl', 'c')  # Copy

    time.sleep(1)  # Give some time to copy to clipboard

    # Close developer tools
    pyautogui.hotkey('ctrl', 'shift', 'i')

    # Get the copied HTML from the clipboard
    page_source = pyperclip.paste()
    return page_source


def contains_simplified_chinese(text):
    # Regular expression to match any Simplified Chinese characters
    chinese_chars = re.findall(r'[\u4e00-\u9fff]', text)
    return bool(chinese_chars), chinese_chars

def refresh_page():
    pyautogui.hotkey('ctrl', 'r')
    time.sleep(1)  # Wait for the page to reload

def process_page():
    # Simulate keypresses to copy and paste
    pyautogui.hotkey('ctrl', 'u')  # Turn on ctrl+u
    time.sleep(4)  # Add a short delay between key presses
    pyautogui.hotkey('ctrl', 'a')  # Select all
    time.sleep(4)  # Add a short delay between key presses
    pyautogui.hotkey('ctrl', 'c')  # Copy
    time.sleep(1)  # Add a short delay between key presses
    pyautogui.hotkey('ctrl', 'w')  # Move to the next page
    time.sleep(1)  # Wait for translation



if __name__ == "__main__":
        # Example usage
    full_dict = {
        "Chapter 80": 'http://example.com/80',
        "Chapter 81": 'http://example.com/81',
        "Chapter 82": 'http://example.com/82',
        "Chapter 83": 'http://example.com/83',
        "Chapter 84": 'http://example.com/84'
    }

    start_number = ''
    end_number = ''
    cycles = 2
    work_dict = working_dictionary(full_dict, start_number, end_number, cycles)
    # print(work_dict)
