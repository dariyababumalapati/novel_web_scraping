import os

from auto_copy.autocopy import orienting_tabs, preload_pages_same_tab, process_page, sav, skip_tab

from useful_operations.name_the_file import name_the_file

from useful_operations.useful_operations import remove_files

from text_editing.useful_text_operations import remove_lines_with_prefixes, replace_words_in_file

from text_editing.line_editing import join_broken_lines

from scrap.config import VariablesCall

from auto_conv.txt_to_epub import txt_to_epub

from share_file.g_drive_upolad import upload_f_to_g_drive

num_pages = 20
  # Change this to the number of pages you want to scrape

reset_file_path = 'text_files/extracted_text.txt'

remove_files(reset_file_path)

orienting_tabs()

preload_pages_same_tab(num_pages)

for _ in range(num_pages):
    process_page()

sav()

skip_tab()

file_path_extracted_text = 'text_files/extracted_text.txt'
chapter_indexes  = name_the_file(file_path_extracted_text)

file_path_raw = f'text_files/chapters_raw/{chapter_indexes[0]}-{chapter_indexes[-1]}_raw.txt'
temp_file = f'text_files/temp_file.txt'
file_path_cleaned = f'text_files/chapters_cleaned/{chapter_indexes[0]}-{chapter_indexes[-1]}_cleaned.txt'


prefixes_to_remove_list = VariablesCall.prefixes_to_remove_list
replacements = VariablesCall.replacements

remove_lines_with_prefixes(file_path_i=file_path_raw, file_path_o=temp_file, prefixes_to_remove=prefixes_to_remove_list)

join_broken_lines(file_path_i=temp_file, file_path_o=file_path_cleaned)

replace_words_in_file(file_path=file_path_cleaned, replacement_words=replacements)

remove_files(file_path_extracted_text, temp_file)

full_file_path = os.path.abspath(file_path_cleaned)

txt_to_epub(full_file_path)

# Section to upolad the converted file to the google drive
dowloads_f_path = "C:/Users/91833/Downloads"

uplaod_file_name = f'{chapter_indexes[0]}-{chapter_indexes[-1]}_cleaned.epub'

g_drive_folder_id = '1D31g6amVH_yiEuNkECC2sDGJJ81J2LhK'

upload_f_to_g_drive(folder_path=dowloads_f_path, file_name=uplaod_file_name, folder_id=g_drive_folder_id)