import time
import pyautogui


# Function to perform actions for each page
def process_page():
    # Simulate keypresses to copy and paste
    pyautogui.hotkey('ctrl', 'shift', 'r')  # Turn on readbee extension
    time.sleep(0.5)  # Add a short delay between key presses
    pyautogui.hotkey('ctrl', 'a')  # Select all
    time.sleep(0.5)  # Add a short delay between key presses
    pyautogui.hotkey('ctrl', 'c')  # Copy
    time.sleep(0.5)  # Add a short delay between key presses
    pyautogui.hotkey('alt', 'tab')  # Switch to Notepad
    time.sleep(0.5)  # Add a short delay between key presses
    pyautogui.hotkey('ctrl', 'v')  # Paste
    time.sleep(0.5)  # Add a short delay between key presses
    pyautogui.press('enter')  # Press Enter twice for readability
    time.sleep(0.5)  # Add a short delay between key presses
    pyautogui.press('enter')
    time.sleep(0.5)  # Add a short delay between key presses
    pyautogui.hotkey('alt', 'tab')  # Switch to Chrome browser
    time.sleep(0.5)  # Add a short delay between key presses
    pyautogui.hotkey('shift', 'right')  # Move to the next page
    time.sleep(3)  # Wait for translation


def preload_pages(num):
    for _ in range(num):
        pyautogui.hotkey('shift', 'right')  # Move to the next page
        time.sleep(3)  # Wait for translation

    pyautogui.hotkey('ctrl', 'tab')  # Move to the next page
    


# Function to save the .txt document
def sav():
    pyautogui.hotkey('alt', 'tab')  # Switch to Notepad
    pyautogui.hotkey('ctrl', 's')  # Save the document
    # Consider adding a prompt or specifying the file path and name

# Function to orient tabs
def orienting_tabs():
    pyautogui.hotkey('alt', 'tab')  # Switch to Notepad
    time.sleep(0.5)  # Add a short delay between key presses

    # Simulate holding 'Alt' key down
    pyautogui.keyDown('alt')

    # Simulate pressing 'Tab' twice
    pyautogui.press('tab')
    time.sleep(0.5)  # Add a short delay between key presses
    pyautogui.press('tab')

    # Release the 'Alt' key
    pyautogui.keyUp('alt')
    time.sleep(0.5)  # Add a short delay between key presses


if __name__ == "__main__":
    # Perform the process for multiple pages
    num_pages = 9  # Change this to the number of pages you want to scrape

    orienting_tabs()

    for _ in range(num_pages):
        process_page()

    sav()
