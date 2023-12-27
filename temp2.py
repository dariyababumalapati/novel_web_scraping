import os
import re

def list_files_in_folder(folder_path):
    files_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            files_list.append(file)
    return files_list

# Replace 'folder_path' with the path to your folder

def get_range(files_list):
    chapters_range = []

    first_number = re.findall(r'\d+', files_list[0])[0]
    chapters_range.append(first_number)

    last_number = re.findall(r'\d+', files_list[-1])[0]
    chapters_range.append(last_number)

    return chapters_range

def missing_chapter_numbers(files_list, chapters_range:list):

    expected_range = range(int(chapters_range[0]), int(chapters_range[-1]) + 1)
    missing_numbers = [num for num in expected_range if f'chapter_{num}.html' not in files_list]

    print("Missing numbers:", missing_numbers)

# print(files_list)

folder_path = 'files/xhtml_files_temp/mhag'
files_list = list_files_in_folder(folder_path)

ch_range = get_range(files_list)

missing_chapter_numbers(files_list, ch_range)