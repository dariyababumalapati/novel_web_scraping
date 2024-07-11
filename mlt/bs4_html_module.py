import requests
from bs4 import BeautifulSoup
import json
import re
import pyperclip


def update_chapter_number(chapter_number):
    json_file = 'tk/inproject_data.json'
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        print(data['chapter_number'])
        data['chapter_number'] = str(chapter_number)

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


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
    return soup.prettify()  

def check_chinese_text(text: str) -> bool:
    # Define a regex pattern that matches Chinese characters
    chinese_pattern = re.compile('[\u4e00-\u9fff]')
    # Return True if any Chinese character is found, otherwise False
    return bool(chinese_pattern.search(text))

def extract_chapter_html(outer_html):
    soup = BeautifulSoup(outer_html, 'html.parser')
    title_element = soup.find('h1', class_='main-title')
    chapter_element = soup.find('div', class_='par fontsize-16')
    html_tag = soup.new_tag('html')
    html_tag['xmlns'] = "http://www.w3.org/1999/xhtml"
    html_tag['xml:lang'] = html_tag.get('lang', 'en')
    html_tag['lang'] = html_tag.get('lang', 'en')

    body_tag = html_tag.find('body') or soup.new_tag('body')

    body_tag.append(chapter_element)
    html_tag.append(title_element)
    html_tag.append(body_tag)

    return html_tag.prettify()

def extract_uu_chapter_html(outer_html):
    soup = BeautifulSoup(outer_html, 'html.parser')

    title_element = soup.find('span', class_='title')
    body_tag = soup.find('div', id='bookContent')

    h1_tag = soup.new_tag('h1')
    html_tag = soup.new_tag('html')
    html_tag['xmlns'] = "http://www.w3.org/1999/xhtml"
    html_tag['xml:lang'] = html_tag.get('lang', 'en')
    html_tag['lang'] = html_tag.get('lang', 'en')

    h1_tag.append(title_element)
    html_tag.append(h1_tag)
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


def replace_words_in_html(html_content:str, replace_words:dict):
    """
    Replace specific words in HTML content with given replacements.

    Args:
    - html_content (str): HTML content as a string.
    - replace_words (dict): Dictionary containing words to replace and their replacements.

    Returns:
    - str: Modified HTML content after replacing words.
    """
    try:
        soup = BeautifulSoup(html_content, 'html.parser')

        for element in soup.descendants:
            if element.name and element.name != 'script':  # Exclude 'script' elements
                for word, replacement in replace_words.items():
                    if element.string and word in element.string:
                        element.string.replace_with(str(element.string).replace(word, replacement))

        modified_html = str(soup)
        return modified_html
    
    except Exception as e:
        print(f"Error occurred while replacing words: {e}")
        return html_content  # Return original content if an error occurs

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


def check_chinese_text(text: str, exception_count) -> bool:
    # Define a regex pattern that matches Chinese characters
    chinese_pattern = re.compile('[\u4e00-\u9fff]')
    # Return True if any Chinese character is found, otherwise False
    if exception_count == 4:
        return False
    else:
        return bool(chinese_pattern.search(text))



if __name__ == "__main__":
    number_of_chapters = 2
    # urls = generate_urls(number_of_chapters)
    # for chapter, url in urls.items():
    #     soup = get_soup(url)
    #     chapter_html = extract_chapter_html(soup)
    #     xhtml_content = convert_html_to_xhtml(chapter_html)

    #     file_name = f"rmf_htmls/{chapter}.html"

    #     with open(file_name, 'w', encoding='utf-8') as file:
    #         file.write(chapter_html)

        
    #     xfile_name = f"rmf_xhtmls/{chapter}.html"

    #     with open(xfile_name, 'w', encoding='utf-8') as file:
    #         file.write(xhtml_content)
    
    # update_chapter_number(number_of_chapters)
    # Get the HTML content from the clipboard
    # 
    # Write the prettified HTML content to the file
    file_path = 'tk/htmls/ot.html'
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Prettify the HTML content
    prettified_html = BeautifulSoup(html_content, 'html.parser').prettify()


    manufactured_html = extract_uu_chapter_html(prettified_html)
    # print(title_element)

    # Define the file path
    file_path = 'tk/htmls/ot4.html'

    # Write the prettified HTML content to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(manufactured_html)