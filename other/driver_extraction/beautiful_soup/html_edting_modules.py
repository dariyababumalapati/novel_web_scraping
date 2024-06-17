from bs4 import BeautifulSoup


def remove_elements_with_certain_texts(html_content, texts_to_remove):
    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all elements containing any of the texts to remove
    elements_to_remove = soup.find_all(text=lambda text: text and any(t in text for t in texts_to_remove))

    # Remove elements containing the specified texts
    for element in elements_to_remove:
        element.extract()

    # Get the modified HTML content
    modified_html = str(soup)

    return modified_html


def replace_words_in_html(html_content, replace_words):
    soup = BeautifulSoup(html_content, 'html.parser')

    for element in soup.descendants:
        if element.name and element.name != 'script':  # Exclude 'script' elements
            for word, replacement in replace_words.items():
                if element.string and word in element.string:
                    element.string.replace_with(str(element.string).replace(word, replacement))

    # Get the modified HTML content
    modified_html = str(soup)
    return modified_html

def replace_dots_with_dash(html_content):
    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_content, 'html.parser')

    for element in soup.find_all():
        if element.string and set(element.string.strip()) == {'.'}:
                element.replace_with('---')

    # Get the modified HTML content
    modified_html = str(soup)
    return modified_html

if __name__ == '__main__':
     print('html_editing_modules.py running in main')