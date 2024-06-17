import requests
from bs4 import BeautifulSoup, Doctype

from lxml import etree

def generate_urls(number):
    urls = {}
    for i in range(1, number+1):
        chapter = f"Chapter {i}"
        url = f"https://gemnovels.com/novel/rome-must-fall/chapter-{i}/"
        urls[chapter] = url
    return urls

def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def extract_chapter_html(soup):
    chapter_div = soup.find('div', class_='chapter-container container mt-4')
    sp_title_div = chapter_div.find('div', class_='sp-title')
    p_elements = chapter_div.find_all('p')

    html_tag = soup.new_tag('html')
    html_tag['xmlns'] = "http://www.w3.org/1999/xhtml"
    html_tag['xml:lang'] = html_tag.get('lang', 'en')
    html_tag['lang'] = html_tag.get('lang', 'en')

    head_tag = html_tag.find('head') or soup.new_tag('head')
    body_tag = html_tag.find('body') or soup.new_tag('body')

    chapter_content_div = soup.new_tag('div', id='chapter_content')

    if sp_title_div:
        chapter_content_div.append(sp_title_div)
    for p in p_elements:
        if p.get_text() == 'Any amount will be greatly appreciated.':
            break
        chapter_content_div.append(p)

    body_tag.append(chapter_content_div)
    html_tag.insert(0, head_tag)
    html_tag.append(body_tag)

    return html_tag.prettify()


def convert_html_to_xhtml(html_code):
    # Parse the HTML code
    soup = BeautifulSoup(html_code, 'html.parser')

    # Add XHTML doctype
    doctype = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">"""

    # Convert Doctype to string and concatenate with prettified soup
    return doctype + '\n' + soup.prettify()

if __name__ == "__main__":
    number_of_chapters = 2
    urls = generate_urls(number_of_chapters)
    for chapter, url in urls.items():
        soup = get_soup(url)
        chapter_html = extract_chapter_html(soup)
        xhtml_content = convert_html_to_xhtml(chapter_html)

        file_name = f"rmf_htmls/{chapter}.html"

        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(chapter_html)

        
        xfile_name = f"rmf_xhtmls/{chapter}.html"

        with open(xfile_name, 'w', encoding='utf-8') as file:
            file.write(xhtml_content)
