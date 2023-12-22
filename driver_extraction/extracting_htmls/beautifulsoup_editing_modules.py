from bs4 import BeautifulSoup

import re

def parse_the_html(html_content):

    soup = BeautifulSoup(html_content, 'html.parser')

    return soup

def remove_elements(html_content):

    soup = parse_the_html(html_content=html_content)
    
    elements_to_remove = soup.find_all(lambda tag: tag.name == 'h1' and 'hide720' in tag.get('class', []) or 
                                                tag.name == 'div' and 'hide720' in tag.get('class', []) or
                                                tag.name == 'div' and "bottom-ad" in tag.get('class', []) or
                                                tag.name == 'div' and tag.get('id') == 'txtright')

    for element in elements_to_remove:
        element.extract()

    return soup


def remove_elements_with_certain_texts(soup, texts_to_remove:list):
    """
    Remove HTML elements containing specified texts.

    Args:
    - soup (BeautifulSoup): The BeautifulSoup object representing the HTML.
    - texts_to_remove (list): A list of strings.
        The function will find and remove HTML elements containing any of the specified texts.

    Returns:
    - BeautifulSoup: The modified BeautifulSoup object after removing elements.
    """

    # Find all elements containing any of the texts to remove
    elements_to_remove = soup.find_all(text=lambda text: text and any(t in text for t in texts_to_remove))

    # Remove elements containing the specified texts
    for element in elements_to_remove:
        element.extract()

    # Get the modified soup
    return soup


def replace_words_in_html(soup, replace_words: dict):
    for element in soup.descendants:
        if element.name and element.name != 'script':  # Exclude 'script' elements
            for replacement, to_replace in replace_words.items():
                if element.string:
                    for word in to_replace:
                        if word in element.string:
                            element.string.replace_with(str(element.string).replace(word, replacement))

    # Get the modified HTML soup
    return soup


def replace_dots_with_dash(soup):

    for element in soup.find_all():
        if element.string and set(element.string.strip()) == {'.'}:
                element.replace_with('---')

    # Get the modified HTML soup
    return soup


def get_chapter_number(soup):

    chapter_element = soup.find(string=lambda text: text and 'Chapter' in text.strip())
    if chapter_element:
        chapter_number = re.findall(r'\d+', chapter_element.get_text())[0]
        return chapter_number

    else:
        print('chapter number is None')
        return None        


def create_html_file(soup, file_path):

    formatted_html = soup.prettify()

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(formatted_html)



if __name__ == '__main__':
    print('beautifulsoup_editing_modules.py is running on main.')

