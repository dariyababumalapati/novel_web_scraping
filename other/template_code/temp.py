from lxml import etree

def convert_html_to_xhtml_with_filepath(input_file_path, output_file_path, output_file_path_temp):

    parser = etree.HTMLParser()
    tree = etree.parse(input_file_path, parser)

    with open(output_file_path, 'wb') as f:
        f.write(etree.tostring(tree, pretty_print=True, method='xml'))
    
    with open(output_file_path_temp, 'wb') as f:
        f.write(etree.tostring(tree, pretty_print=True, method='xml'))

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

def convert_html_to_xhtml_with_sp(html_content, file_path='temp_kgm.html'):

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    parser = etree.HTMLParser()
    tree = etree.parse(file_path, parser)

    
    with open(file_path, 'wb') as f:
        f.write(etree.tostring(tree, pretty_print=True, method='xml'))

    # output_content = etree.tostring(tree, pretty_print=True, method='xml', encoding='unicode')
    # with open(file_path, 'rb', encoding='utf-8') as f:
    #     xhtml_content = f.read()

    # print(output_content)

if __name__ == '__main__':

    filepath = 'kgm/rh_c.html'

    ofp = 'kgm/lxml/rh_cx3.html'

    ofpt = 'kgm/lxmlo/rh_cxo.html'

    # convert_html_to_xhtml_with_filepath(filepath, ofp, ofpt)

    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()


    convert_html_to_xhtml_with_sp(html_content)

    # with open(ofp, 'w', encoding='utf-8') as f:
    #     f.write(soup)
