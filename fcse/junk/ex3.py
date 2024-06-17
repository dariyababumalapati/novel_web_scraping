from bs4_html_module import convert_text_file_to_html_document, create_html_document, convert_html_to_xhtml

import json
stop_number = 110

json_file = f'fcse/chapters_data_{stop_number}.json'

print(json_file)

with open(json_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

text_file = 'fcse/99.txt'
new_data = {}

for chapter_title, chapter_data in data.items():

    chapter_content = chapter_data

    with open(text_file, 'w', encoding='utf-8') as file:
        file.write(chapter_content)


    html_content = convert_text_file_to_html_document(text_file)

    xhtml_content = convert_html_to_xhtml(html_content)

    new_data[chapter_title] = xhtml_content

    new_data_file = 'fcse/new_data.json'

    with open(new_data_file, 'w', encoding='utf-8') as file:
        json.dump(new_data, file, ensure_ascii=False, indent=4)