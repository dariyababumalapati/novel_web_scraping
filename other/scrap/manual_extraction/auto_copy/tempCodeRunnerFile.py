import pyautogui
import time


def sav():
    pyautogui.hotkey('alt', 'tab')  # Switch to Notepad
    time.sleep(1)  # Add a short delay between key presses
    pyautogui.hotkey('ctrl', 's')  # Save the document
    time.sleep(1)
    pyautogui.typewrite('xtracted_text')
    time.sleep(1)
    pyautogui.press('enter')

sav()