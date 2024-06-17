from bs4 import BeautifulSoup

def convert_html_to_xhtml(html_content):
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
