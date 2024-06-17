import os
import json
from bs4_html_module import generate_urls, get_soup, extract_chapter_html, convert_html_to_xhtml

def write_html_content(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def store_chapter_data(chapter_number, chapter_html):
    data = {
        "chapter_number": chapter_number,
        "chapter_html": chapter_html
    }
    json_data = json.dumps(data)

    json_file_name = f"chapter_{chapter_number}.json"
    with open(json_file_name, 'w') as file:
        file.write(json_data)

def store_xhtml_data(chapter_number, xhtml_content):
    data = {
        "chapter_number": chapter_number,
        "xhtml_content": xhtml_content
    }
    json_data = json.dumps(data)

    json_file_name = f"xhtml_{chapter_number}.json"
    with open(json_file_name, 'w') as file:
        file.write(json_data)

def main(number_of_chapters=1):
    urls = generate_urls(number_of_chapters)

    # html_directory = "rmf_htmls"
    # xhtml_directory = "rmf_xhtmls"

    # create_directory(html_directory)
    # create_directory(xhtml_directory)

    chapter_htmls = {}
    xhtml_contents = {}

    for chapter, url in urls.items():
        soup = get_soup(url)
        chapter_html = extract_chapter_html(soup)
        xhtml_content = convert_html_to_xhtml(chapter_html)

        # html_file_name = f"{html_directory}/{chapter}.html"
        # xhtml_file_name = f"{xhtml_directory}/{chapter}.html"

        # write_html_content(html_file_name, chapter_html)
        # write_html_content(xhtml_file_name, xhtml_content)

        chapter_htmls[chapter] = chapter_html
        xhtml_contents[chapter] = xhtml_content

        store_chapter_data(chapter, chapter_html)
        store_xhtml_data(chapter, xhtml_content)

    return chapter_htmls, xhtml_contents

if __name__ == "__main__":
    chapter_htmls, xhtml_contents = main(49)
    
    html_file_name = 'rmf/rmf_html.json'
    xhtml_file_name = 'rmf/rmf_xhtml.json'
    
    with open(html_file_name, 'w', encoding='utf-8') as html_file:
        json.dump(chapter_htmls, html_file, ensure_ascii=False)

    with open(xhtml_file_name, 'w', encoding='utf-8') as xhtml_file:
        json.dump(xhtml_contents, xhtml_file, ensure_ascii=False)
