from auto_copy.autocopy import orienting_tabs, process_page, sav, preload_pages
from useful_operations import open_txt, clean_text


file_path_address = '323.txt'
num_pages = 20  # Change this to the number of pages you want to scrape

open_txt(file_path_address)

orienting_tabs()

preload_pages(num_pages)

for _ in range(num_pages):
    process_page()

sav()

clean_text(file_path_address)