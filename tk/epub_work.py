
from share_file.g_drive_upolad import upload_f_to_g_drive

from epub_maker import EpubMaker

import json

# Read the JSON file


book_title = 'tk'

with open(f'{book_title}/inproject_data.json', 'r', encoding='utf-8') as file:
    inproject_data = json.load(file)

chapter_number = inproject_data['chapter_number']

json_file_path = f'{book_title}/jsons/chapters_data_{chapter_number}.json'

# json_file_path = f'tk/jsons/chapters_data_{chapter_number}.json'

with open(json_file_path, 'r', encoding='utf-8') as file:
    chapters_data = json.load(file)

file_name = f"{book_title}_{chapter_number}"


book_information = {
    "book_title": f"The King {chapter_number}",
    "author_name": "Han Yue",
    "language": "en",
    "image_file_path": "tk/tk.jpeg",
    "chapters_dict": chapters_data,
    "epub_file_name": file_name,
    "destination_directory": "C:/Users/91833/OneDrive/Desktop/books",
    }

king_of_gods = EpubMaker()
king_of_gods.make_epub(book_information)

destination_dir = f"C:/Users/91833/OneDrive/Desktop/books/{file_name}.epub"
drive_folder_id = inproject_data['d_folder_list'][book_title]

upload_f_to_g_drive(file_name=destination_dir, folder_id=drive_folder_id)

