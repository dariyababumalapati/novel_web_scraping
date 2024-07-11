import pyperclip

from autocopy import *

from autocopy import remove_content_between_keywords

from txt_to_epub import txt_to_epub
from share_file.g_drive_upolad import upload_f_to_g_drive


number_of_chapters = 40
chapter_number = 100

novels = ['ree', 'ra', 'sl']

novel = novels[2]

file_path = rf"C:\Users\91833\OneDrive\Desktop\books\{novel}\{novel}_{chapter_number}.txt"
up_file_path = rf"C:\Users\91833\OneDrive\Desktop\books\{novel}\update\{novel}_{chapter_number}.txt"

url = "https://convertio.co/txt-epub/"

next_tab()

for _ in range(number_of_chapters):
    process_page()

    chapter_content = pyperclip.paste()

    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(f"{chapter_content}\n\n\n")


next_tab()

eliminate_words = {
        'UU': 'et',
    }

remove_content_between_keywords(file_path, up_file_path, eliminate_words)

txt_to_epub(up_file_path)

ree = "1AidBHDjC0QrafhxekBe5SFtqxJzL4Nli"
ra = "11cOTl6N5m9whAcPrQnCGksNRAE02GfGC"
file_name = rf"C:\Users\91833\Downloads\{novel}_{chapter_number}.epub"

upload_f_to_g_drive(file_name=file_name, folder_id=ra)
