import json

from extract_html_module_tk import initiate_driver, wait_to_translate, click_consent_button, scroll_to_bottom, scroll_to_top, copy_full_html

from bs4 import BeautifulSoup
from bs4_html_module import check_chinese_text, extract_uu_chapter_html, convert_html_to_xhtml, replace_words_in_html

from epub_maker import EpubMaker
from share_file.g_drive_upolad import upload_f_to_g_drive


start_number = 526

stop_number = 550


replace_words = {'’': "'", '“': '"', '”': '"', '—': '-', '…': '...', '‘': "'"}

chapters_data = {}


output_file = f'tk/jsons/chapters_data_{stop_number}.json'

primary_url = 'https://m.uuks.org/b/57664/72080526.html'

driver = initiate_driver(primary_url)
driver.maximize_window()
click_consent_button(driver)
driver = wait_to_translate(driver)



for i in range(start_number, stop_number+1):
    url = f'https://m.uuks.org/b/57664/72080{i}.html'
    title = f"Chapter {i}"

    driver.get(url)
    relay = True

    while relay:
        driver.refresh()

        scroll_to_bottom(driver)
        outer_html = copy_full_html(driver)
        html = extract_uu_chapter_html(outer_html)
        html = replace_words_in_html(html, replace_words)
        relay = check_chinese_text(html)

        if relay:
            scroll_to_top(driver)
        
        xhtml = convert_html_to_xhtml(html)
        # soup = BeautifulSoup(xhtml, 'html.parser')
        # with open('tk/htmls/test_2.html', 'w', encoding='utf-8') as file:
        #     file.write(soup.prettify())
        chapters_data[title] = xhtml
        print(f"{title} done.")

        # Write chapters_data to f'tk/jsons/chapters_data{x}.json'
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(chapters_data, file, ensure_ascii=False, indent=4)
            

epub_file_name = f"tk_{stop_number}"

# Read from 'book_info.json'
with open('tk/book_info.json', 'r', encoding='utf-8') as file:
    book_info = json.load(file)

book_info['book_title'] = f"The King {stop_number}"
book_info['chapters_dict'] = chapters_data
book_info['epub_file_name'] = epub_file_name


# Create an instance of EpubMaker
the_king = EpubMaker()
the_king.make_epub(book_info)

# send the epub file to Google Drive
destination_file = f"{book_info['destination_directory']}/{epub_file_name}.epub"
drive_folder_id = book_info['drive_folder_id']

upload_f_to_g_drive(file_name=destination_file, folder_id=drive_folder_id)

