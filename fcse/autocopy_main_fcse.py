import json
import pyperclip

from autocopy import next_tab, paste_and_enter, process_page, replace_words_in_file

from bs4_html_module import check_chinese_text, convert_text_file_to_html_document, update_chapter_number

import pyautogui

import time



"""
The number of chapters to process. This value is used to control the loop that processes each chapter.
"""
start_number = 165

stop_number = 190

update_chapter_number(stop_number)

json_file = f'fcse/json_files/chapters_data_{stop_number}.json'

main_link = 'https://www.uuks.org/b/53573/669661.html'

next_tab()


text_file = 'fcse/clip_board.txt'

replace_words = {
    'Close': '',
    '_From City-State to Empire_UU Reading': '',
    'If you like this work, you are welcome to vote for recommendations and monthly tickets at Qidian. Your support is my greatest motivation.': '',
    '(To be continued. If you like this work, you are welcome to vote for recommendations and monthly tickets at Qidian. Your support is my greatest motivation.)': '',
}

chapters_data = {}

for x in range(start_number, stop_number+1):
    chapter_number = f'Chapter {x}'
    chapter_url = f'https://www.uuks.org/b/53573/66966{x}.html'

    pyperclip.copy(chapter_url)

    paste_and_enter()
    time.sleep(4)

    relay = True

    while relay:
        time.sleep(3)
        process_page()
        chapter_content = pyperclip.paste()

        relay = check_chinese_text(chapter_content)

        if not relay:
            chapter_content = chapter_content.replace('Close', '')
            chapter_content = chapter_content.replace('_From City-State to Empire_UU Reading', '')
            with open(text_file, 'w', encoding='utf-8') as f:
                f.write(chapter_content)

            replace_words_in_file(text_file, replace_words)

            xhtml_content = convert_text_file_to_html_document(text_file)

            chapters_data[chapter_number] = xhtml_content

            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(chapters_data, f, ensure_ascii=False, indent=4)
        else:
            pyautogui.hotkey('ctrl', 'r')  # Press Ctrl+R
            time.sleep(2)  # Add a short delay between key presses
    

time.sleep(3)



next_tab()

# ree = "1AidBHDjC0QrafhxekBe5SFtqxJzL4Nli"
# ree_texts = '1cGFKS7-vIXZi4T6YaVoQrcW6hrQNCtly'
# ra = "11cOTl6N5m9whAcPrQnCGksNRAE02GfGC"
# kor = "1YsGrSdHHRLRvV2bBvQuWNlnWfsm0AMC_"
# ming = "11sbPdj5jBxVf76ddkIvCjU3ASBKdlKT4"
# rmf = '17NsNIO9k4v2IU1x-fmRqpluWEv_ATcTJ'
# fcse = '133H_cn0urMFlVOh-iSeShe_6wwVNZrz2'
# file_name = rf"C:\Users\91833\Downloads\{novel}_{stop_number}.epub"

# upload_f_to_g_drive(file_name=up_file_path, folder_id=ree_texts)

# txt_to_epub(up_file_path)
# upload_f_to_g_drive(file_name=file_name, folder_id=fcse)