from share_file.g_drive_upolad import upload_f_to_g_drive
import json

stop_number = 600

epub_file_name = f"tk_{stop_number}"

# Read from 'book_info.json'
with open('tk/book_info.json', 'r', encoding='utf-8') as file:
    book_info = json.load(file)


# send the epub file to Google Drive
destination_file = f"{book_info['destination_directory']}/{epub_file_name}.epub"
drive_folder_id = book_info['drive_folder_id']

upload_f_to_g_drive(file_name=destination_file, folder_id=drive_folder_id)

