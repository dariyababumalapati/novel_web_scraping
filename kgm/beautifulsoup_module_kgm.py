from bs4 import BeautifulSoup, Tag

from lxml import etree


def create_html_file(html_content, file_path):
    """
    Create an HTML file with formatted content.

    Args:
    - html_content (str): HTML content as a string.
    - file_path (str): File path to save the HTML content.

    Returns:
    - None
    """
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        formatted_html = soup.prettify()

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(formatted_html)

        print(f"{file_path} created.")
    
    except Exception as e:
        print(f"Error occurred while creating HTML file: {e}")


def remove_elements_with_certain_texts(html_content: str, texts_to_remove: list):
    """
    Remove elements from HTML content containing specific texts.

    Args:
    - html_content (str): HTML content as a string.
    - texts_to_remove (list): List of texts to identify elements for removal.

    Returns:
    - str: Modified HTML content after removing specified elements.
    """
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        elements_to_remove = soup.find_all(text=lambda text: text and any(t in text for t in texts_to_remove))

        for element in elements_to_remove:
            element.extract()

        modified_html = str(soup)
        return modified_html
    
    except Exception as e:
        print(f"Error occurred while removing elements: {e}")
        return html_content  # Return original content if an error occurs


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


def replace_dots_with_dash(html_content):
    """
    Replace standalone dots in HTML content with dashes.

    Args:
    - html_content (str): HTML content as a string.

    Returns:
    - str: Modified HTML content after replacing dots with dashes.
    """
    try:
        soup = BeautifulSoup(html_content, 'html.parser')

        for element in soup.find_all():
            if element.string and set(element.string.strip()) == {'.'}:
                    element.replace_with('---')

        modified_html = str(soup)
        return modified_html
    
    except Exception as e:
        print(f"Error occurred while replacing dots: {e}")
        return html_content  # Return original content if an error occurs

def merge_elements(html_content):
    """
    Merge two elements found in the HTML content into a new <div> element.

    Args:
    - html_content (str): HTML content as a string.

    Returns:
    - Tag or None: Returns the newly created <div> element with the merged content,
                   or None if elements are not found or merge is unsuccessful.
    """
    try:
        soup = BeautifulSoup(html_content, 'html.parser')

        element_1 = soup.find('h1', id='timu')
        element_2 = soup.find('div', class_='uu_cont', id='contentbox')

        # Check if both elements exist before merging
        if element_1 and element_2:
            # Create a new empty <div> element with the ID 'main'
            new_div = Tag(builder=soup.builder, name='div', attrs={'id': 'main'})

            # Create <br> elements
            br1 = soup.new_tag('br')
            br2 = soup.new_tag('br')

            # Append elements to the new <div> in the desired order
            new_div.append(element_1)
            new_div.append(br1)
            new_div.append(br2)
            new_div.append(element_2)

            formatted_html = new_div.prettify()

            return formatted_html

    except Exception as e:
        print(f"Error occurred: {e}")

    return None  # Return None if elements are not found or merge is unsuccessful

def convert_html_to_xhtml_bs(html_content):
    """
    Convert HTML content to XHTML format.

    Args:
    - html_content (str): HTML content to be converted to XHTML.

    Returns:
    - str or None: Returns the converted XHTML content if successful, otherwise returns None.
    """
    try:
        # Create a BeautifulSoup object from the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Convert the parsed soup object to XML/XHTML format
        xhtml_content = soup.prettify(formatter='xml')
        
        return xhtml_content

    except Exception as e:
        print(f"An error occurred while converting HTML to XHTML: {e}")
        return None


def convert_html_to_xhtml_kgm(html_content, file_path='temp_kgm.html'):

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    parser = etree.HTMLParser()
    tree = etree.parse(file_path, parser)

    output_content = etree.tostring(tree, pretty_print=True, method='xml', encoding='unicode')

    return output_content


def convert_html_to_xhtml(html_content:str):
    """
    Convert HTML content to XHTML format.

    Args:
    - html_content (str): HTML content to be converted to XHTML.

    Returns:
    - str or None: Returns the converted XHTML content if successful, otherwise returns None.
    """
    try:
        # Create an HTML parser
        parser = etree.HTMLParser()

        # Parse the HTML content into an XML tree
        tree = etree.fromstring(html_content, parser)
        
        # Convert the XML tree to XHTML content
        output_content = etree.tostring(tree, pretty_print=True, method='xml', encoding='unicode')
        return output_content

    except etree.Error as e:
        print(f"Error occurred while converting HTML to XHTML: {e}")
        return None
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
        return None

def check_chinese_text(html_content:str):
    soup = BeautifulSoup(html_content, 'html.parser')
    


if __name__ == '__main__':
     print('html_editing_modules.py running in main')