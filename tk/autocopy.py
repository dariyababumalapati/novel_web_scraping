import time
import pyautogui
import pyperclip
import json

def update_chapter_number(chapter_number):
    with open('inproject_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        data['chapter_number'] = chapter_number

    with open('inproject_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def get_inproject_data():
    with open('inproject_data.json', 'r') as f:
        data = json.load(f)
        chapter_number = data['chapter_number']
        d_folder_list = data['d_folder_list']
        novels = data['novels']

        return chapter_number, d_folder_list, novels

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
    time.sleep(0.5)  # Add a short delay between key presses

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
    # Perform the process for multiple pages
    num_pages = 9  # Change this to the number of pages you want to scrape

    for _ in range(num_pages):
        process_page()

