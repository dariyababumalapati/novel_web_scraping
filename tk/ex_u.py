import pyautogui
import time
from pynput.keyboard import Key, Controller
import pyperclip

from bs4 import BeautifulSoup

from autocopy import next_tab


keyboard = Controller()

def open_devtools():
    # Press Ctrl+Shift+I to open DevTools
    with keyboard.pressed(Key.ctrl):
        with keyboard.pressed(Key.shift):
            keyboard.press('i')
            keyboard.release('i')
    time.sleep(2)  # Wait for DevTools to open

def select_html_element():
    # Navigate to the Elements tab (usually already opened)
    # Select the root element (usually `<html>`)
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(1)
    pyautogui.typewrite('<html')
    time.sleep(1)
    pyautogui.press('esc')

def copy_outer_html():
    pyautogui.hotkey('ctrl', 'c')

def main():
    open_devtools()
    select_html_element()
    copy_outer_html()
    print("HTML copied to clipboard. You can paste it now.")

if __name__ == "__main__":
    next_tab()
    # time.sleep(5)  # Give yourself 5 seconds to switch to the browser
    main()
    next_tab()

    raw_html = pyperclip.paste()
    soup = BeautifulSoup(raw_html, 'html.parser')
    html_pre = soup.prettify()
    
    with open('c1.html', 'w', encoding='utf-8') as file:
        file.write(html_pre)