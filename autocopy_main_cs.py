import pyperclip

from autocopy import *

from cleaned_text import refine_text_file

from txt_to_epub import txt_to_epub
from share_file.g_drive_upolad import upload_f_to_g_drive


"""
The number of chapters to process. This value is used to control the loop that processes each chapter.
"""
number_of_chapters = 2
chapter_number = ch_number(number_of_chapters)

novels = ['ree', 'ra', 'kor', 'nep', 'ming', 'rmf']

main_link = 'https://www.uuks.org/b/53573/669661.html'

novel = novels[4]

file_path = rf"C:\Users\91833\OneDrive\Desktop\books\{novel}\{novel}_{chapter_number}.txt"
up_file_path = rf"C:\Users\91833\OneDrive\Desktop\books\{novel}\update\{novel}_{chapter_number}.txt"

url = "https://convertio.co/txt-epub/"

next_tab()

for x in range(1, 51):
    chapter_url = f'https://www.uuks.org/b/53573/66966{x}.html'

for _ in range(number_of_chapters):
    process_page()

    chapter_content = pyperclip.paste()

    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(f"{chapter_content}\n\n\n")


next_tab()

replacement_pairs = [('I was reborn as Zhu Yunwen-', ''), ('-69 Book Bar', '')]
unwanted_string = 'Author: Hanmei Jingxue'

refine_text_file(file_path, up_file_path, replacement_pairs, unwanted_string)

ree = "1AidBHDjC0QrafhxekBe5SFtqxJzL4Nli"
ree_texts = '1cGFKS7-vIXZi4T6YaVoQrcW6hrQNCtly'
ra = "11cOTl6N5m9whAcPrQnCGksNRAE02GfGC"
kor = "1YsGrSdHHRLRvV2bBvQuWNlnWfsm0AMC_"
ming = "11sbPdj5jBxVf76ddkIvCjU3ASBKdlKT4"
rmf = '17NsNIO9k4v2IU1x-fmRqpluWEv_ATcTJ'
file_name = rf"C:\Users\91833\Downloads\{novel}_{chapter_number}.epub"

upload_f_to_g_drive(file_name=up_file_path, folder_id=ree_texts)

txt_to_epub(up_file_path)
upload_f_to_g_drive(file_name=file_name, folder_id=ming)
  