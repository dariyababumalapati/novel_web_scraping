from bs4 import BeautifulSoup, Tag


class HTMLEditor:
    """
    A class for editing HTML content.

    Attributes:
    - html_content (str): The HTML content to be edited.
    """

    def __init__(self, html_content):
        """
        Initialize the HTMLEditor class with HTML content.

        Args:
        - html_content (str): The HTML content to be edited.
        """
        self.html_content = html_content

    def create_html_file(self, file_path):
        """
        Create an HTML file with formatted content.

        Args:
        - file_path (str): File path to save the HTML content.

        Returns:
        - None
        """
        try:
            soup = BeautifulSoup(self.html_content, 'html.parser')
            formatted_html = soup.prettify()

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(formatted_html)

            print(f"{file_path} created.")
        
        except Exception as e:
            print(f"Error occurred while creating HTML file: {e}")

    def convert_html_to_xhtml(self):
        """
        Convert HTML content to XHTML format.

        Returns:
        - str or None: Returns the converted XHTML content if successful, otherwise returns None.
        """
        try:
            soup = BeautifulSoup(self.html_content, 'html.parser')
            xhtml_content = soup.prettify(formatter='xml')
            return xhtml_content
        
        except Exception as e:
            print(f"An error occurred while converting HTML to XHTML: {e}")
            return None

    def remove_elements_with_certain_texts(self, texts_to_remove):
        """
        Remove elements from HTML content containing specific texts.

        Args:
        - texts_to_remove (list): List of texts to identify elements for removal.

        Returns:
        - str: Modified HTML content after removing specified elements.
        """
        try:
            soup = BeautifulSoup(self.html_content, 'html.parser')
            elements_to_remove = soup.find_all(text=lambda text: text and any(t in text for t in texts_to_remove))

            for element in elements_to_remove:
                element.extract()

            modified_html = str(soup)
            return modified_html
        
        except Exception as e:
            print(f"Error occurred while removing elements: {e}")
            return self.html_content  # Return original content if an error occurs

    # Other methods for editing HTML content...
    
    def replace_words_in_html(self, replace_words:dict):
        """
        Replace specific words in HTML content with given replacements.

        Args:
        - html_content (str): HTML content as a string.
        - replace_words (dict): Dictionary containing words to replace and their replacements.

        Returns:
        - str: Modified HTML content after replacing words.
        """
        try:
            soup = BeautifulSoup(self.html_content, 'html.parser')

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


if __name__ == '__main__':
    print('HTMLEditor class defined.')
