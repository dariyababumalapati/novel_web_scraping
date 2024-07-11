import requests
from bs4 import BeautifulSoup, Doctype
import json
from lxml import etree
import re

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

def extract_chapter_html(outer_html):
    soup = BeautifulSoup(outer_html, 'html.parser')
    title_element = soup.find('h1', class_='chapter-title')
    chapter_element = soup.find('div', id='article')

    html_tag = soup.new_tag('html')
    html_tag['xmlns'] = "http://www.w3.org/1999/xhtml"
    html_tag['xml:lang'] = html_tag.get('lang', 'en')
    html_tag['lang'] = html_tag.get('lang', 'en')

    body_tag = html_tag.find('body') or soup.new_tag('body')

    body_tag.append(chapter_element)
    html_tag.append(title_element)
    html_tag.append(body_tag)

    return html_tag.prettify()

def convert_text_to_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Split the text into paragraphs based on double newline
    paragraphs = text.split('\n\n')
    
    # Create a new BeautifulSoup object
    soup = BeautifulSoup("", 'html.parser')
    
    # Create a new div element with id 'chapter-material'
    div = soup.new_tag('div', id='chapter-material')
    
    # Add each paragraph wrapped in <p> tags inside the div
    for paragraph in paragraphs:
        p_tag = soup.new_tag('p')
        p_tag.string = paragraph.strip()
        div.append(p_tag)
    
    # Add the div to the soup
    soup.append(div)
    
    # Return the prettified HTML content
    return soup.prettify()

def create_html_document(chapter_content):
    # Initialize BeautifulSoup with an empty document
    soup = BeautifulSoup('', 'html.parser')

    # Create the <html> tag with the required attributes
    html_tag = soup.new_tag('html')
    html_tag['xmlns'] = "http://www.w3.org/1999/xhtml"
    html_tag['xml:lang'] = 'en'
    html_tag['lang'] = 'en'

    # Create the <head> and <body> tags
    head_tag = soup.new_tag('head')
    body_tag = soup.new_tag('body')


    # Create a new <div> for the chapter content
    chapter_content_div = soup.new_tag('div', id='chapter_content')

    # Append the sp-title <div> to the chapter content
    chapter_content_div.append(chapter_content)

    # Append the chapter content <div> to the <body>
    body_tag.append(chapter_content_div)

    # Append <head> and <body> to the <html> tag
    html_tag.append(head_tag)
    html_tag.append(body_tag)

    # Append the <html> tag to the soup
    soup.append(html_tag)

    # Return the prettified HTML string
    return soup.prettify()


def convert_text_file_to_html_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Split the text into paragraphs based on double newline
    paragraphs = text.split('\n\n')
    
    # Create a new BeautifulSoup object for the chapter content
    soup = BeautifulSoup("", 'html.parser')
    
    # Create a new div element with id 'chapter_content'
    div = soup.new_tag('div', id='chapter_content')
    
    # Add each paragraph wrapped in <p> tags inside the div
    for paragraph in paragraphs:
        stripped_paragraph = paragraph.strip()
        if stripped_paragraph:  # Only add non-empty paragraphs
            p_tag = soup.new_tag('p')
            p_tag.string = stripped_paragraph
            div.append(p_tag)
        # p_tag = soup.new_tag('p')
        # p_tag.string = paragraph.strip()
        # div.append(p_tag)
    
    # Now create the full HTML document
    doc_soup = BeautifulSoup('', 'html.parser')

    # Create the <html> tag with the required attributes
    html_tag = doc_soup.new_tag('html')
    html_tag['xmlns'] = "http://www.w3.org/1999/xhtml"
    html_tag['xml:lang'] = 'en'
    html_tag['lang'] = 'en'

    # Create the <head> and <body> tags
    head_tag = doc_soup.new_tag('head')
    body_tag = doc_soup.new_tag('body')

    # Append the chapter content <div> to the <body>
    body_tag.append(div)

    # Append <head> and <body> to the <html> tag
    html_tag.append(head_tag)
    html_tag.append(body_tag)

    # Append the <html> tag to the soup
    doc_soup.append(html_tag)

    # Return the prettified HTML string
    return doc_soup.prettify()


def convert_html_to_xhtml(html_code):
    # Parse the HTML code
    soup = BeautifulSoup(html_code, 'html.parser')

    # Add XHTML doctype
    doctype = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">"""

    # Convert Doctype to string and concatenate with prettified soup
    return doctype + '\n' + soup.prettify()


<<<<<<< HEAD
def check_chinese_text(text: str, relay) -> bool:
    # Define a regex pattern that matches Chinese characters
    chinese_pattern = re.compile('[\u4e00-\u9fff]')
    # Return True if any Chinese character is found, otherwise False
    relay = bool(chinese_pattern.search(text))
    return relay
    # return bool(chinese_pattern.search(text))
=======
def check_chinese_text(text: str) -> bool:
    # Define a regex pattern that matches Chinese characters
    chinese_pattern = re.compile('[\u4e00-\u9fff]')
    # Return True if any Chinese character is found, otherwise False
    return bool(chinese_pattern.search(text))
>>>>>>> dca2e1185edd59f6ea541d656791141560c15841


def update_chapter_number(chapter_number):
    with open('fcse/inproject_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        data['chapter_number'] = chapter_number

    with open('fcse/inproject_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

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
