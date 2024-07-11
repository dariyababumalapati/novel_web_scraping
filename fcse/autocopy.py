import time
import pyautogui
import pyperclip
import json


def get_inproject_data():
    with open('inproject_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        chapter_number = data['chapter_number']
        d_folder_list = data['d_folder_list']
        novels = data['novels']

        return chapter_number, d_folder_list, novels

def update_chapter_number(chapter_number):
    with open('inproject_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        data['chapter_number'] = chapter_number

    with open('inproject_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def next_tab():
    pyautogui.hotkey('alt', 'tab')  # Switch to Notepad
    time.sleep(0.5)  # Add a short delay between key presses

def scroll_down():
    for _ in range(5):
        pyautogui.scroll(-500)
        time.sleep(1)  # Add a short delay between key presses

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

    pyautogui.hotkey('alt', 'tab')  # Switch to Notepad
    time.sleep(0.5)  # Add a short delay between key presses


def process_page():
    # Simulate keypresses to copy and paste
    pyautogui.hotkey('ctrl', 'shift', 'r')  # Turn on readbee extension
    time.sleep(0.5)  # Add a short delay between key presses
    scroll_down()
    time.sleep(0.5)  # Add a short delay between key presses
    pyautogui.hotkey('ctrl', 'a')  # Select all
    time.sleep(0.5)  # Add a short delay between key presses
    pyautogui.hotkey('ctrl', 'c')  # Copy
    time.sleep(3)  # Wait for translation

# Function to perform actions for each page

# Function to save the .txt document
def sav(file_name: str):
    
    if file_name:
        pyautogui.hotkey('alt', 'tab')  # Switch to Notepad
        time.sleep(1)
        pyautogui.hotkey('ctrl', 's')  # Save the document
        time.sleep(1)
        pyautogui.typewrite(file_name)
        time.sleep(1)
        pyautogui.press('enter')

    else:
        pyautogui.hotkey('alt', 'tab')  # Switch to Notepad
        time.sleep(1)
        pyautogui.hotkey('ctrl', 's')  # Save the document
        time.sleep(1)
        pyautogui.typewrite('extracted_text')
        time.sleep(1)
        pyautogui.press('enter')

def skip_tab():

    pyautogui.keyDown('alt')

    # Simulate pressing 'Tab' twice
    pyautogui.press('tab')
    time.sleep(0.5)  # Add a short delay between key presses
    pyautogui.press('tab')

    # Release the 'Alt' key
    pyautogui.keyUp('alt')
    time.sleep(0.5)  # Add a short delay between key presses

def replace_words_in_file(file_path, replacement_words):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        for old_word, new_word in replacement_words.items():
            content = content.replace(old_word, new_word)

        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied while working with '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


def remove_lines_starting_with(filename, string_to_remove):
    # Read the file and store lines that don't start with the specified string
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line for line in lines if not line.startswith(string_to_remove)]

    # Write the modified content back to the file
    with open(filename, 'w') as file:
        file.writelines(lines)


def remove_content_between_keywords(file_path, update_file_path, keyword_pairs):
    """
    Remove content from a file between specified start and end keywords.
    
    Args:
    - file_path (str): The path to the input text file.
    - update_file_path (str): The path to the output text file.
    - keyword_pairs (dict): Dictionary with start_keyword as keys and end_keyword as values.
    """

    update_list = []
    # Read the content of the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        content_list = file.readlines()

    for content in content_list:
        modified_content = content
        for start_keyword, end_keyword in keyword_pairs.items():
            start_index = modified_content.find(start_keyword)
            end_index = modified_content.find(end_keyword, start_index + len(start_keyword))
            
            if start_index != -1 and end_index != -1:
                # Delete the content between the keywords along with the keywords themselves
                modified_content = modified_content[:start_index] + modified_content[end_index + len(end_keyword):]
        
        update_list.append(modified_content)
        updated_lines = [line for line in update_list if not line.startswith('Close')]

    # Write the modified content back to the file
    with open(update_file_path, 'w', encoding='utf-8') as file:
        for line in updated_lines:
            file.write(line)

    print(f'{update_file_path} created.')


#for the 'from city-state to empire'
def paste_and_enter():
    pyautogui.hotkey('ctrl', 'l')  # Press Ctrl+L
    time.sleep(0.5)  # Add a short delay between key presses
    pyautogui.hotkey('ctrl', 'v')  # Press Ctrl+L
    time.sleep(0.5)  # Add a short delay between key presses
    pyautogui.press('enter')  # Press Enter
    time.sleep(1)  # Add a short delay between key presses

def refresh_page():
    pyautogui.hotkey('ctrl', 'r')  # Press Ctrl+R
    time.sleep(2)  # Add a short delay between key presses

def previous():
    pyautogui.hotkey('alt', 'left')  # Switch to the next tab
    time.sleep(0.5)  # Add a short delay between key presses


if __name__ == "__main__":
    # Perform the process for multiple pages
    num_pages = 9  # Change this to the number of pages you want to scrape

    orienting_tabs()

    for _ in range(num_pages):
        process_page()

    sav()
