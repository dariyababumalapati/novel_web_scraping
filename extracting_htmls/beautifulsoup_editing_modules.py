from bs4 import BeautifulSoup

import re

def remove_elements(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    elements_to_remove = soup.find_all(lambda tag: tag.name == 'h1' and 'hide720' in tag.get('class', []) or 
                                                tag.name == 'div' and 'hide720' in tag.get('class', []) or
                                                tag.name == 'div' and tag.get('id') == 'txtright')

    for element in elements_to_remove:
        element.extract()

# Find the element with string '(End of chapter)'
    end_of_chapter_element = soup.find(string=lambda text: text and '(End of chapter)' in text.strip())

# Remove all elements after the end_of_chapter_element
    if end_of_chapter_element:
        # Get the grandparent of the end_of_chapter_element
        grandparent = end_of_chapter_element.find_parent().find_parent()

        
        # Extract the parent and all its siblings
        while grandparent.next_sibling:
            grandparent.next_sibling.extract()

    return soup

def create_number(soup):
    chapter_element = soup.find(string=lambda text: text and 'Chapter' in text.strip())
    if chapter_element:
        chapter_number = re.findall(r'\d+', chapter_element.get_text())[0]
        return chapter_number

    else:
        print('None')
        return None        
    
def create_html_file(soup, file_path):
    formatted_html = soup.prettify()

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(formatted_html)



if __name__ == '__main__':
    print('beautifulsoup_editing_modules.py is running on main.')