from lxml import etree

def convert_html_to_xhtml(input_file, output_file):
    # parse the HTML
    parser = etree.HTMLParser()
    tree = etree.parse(input_file, parser)

    # write the XHTML to the output file
    with open(output_file, 'wb') as f:
        f.write(etree.tostring(tree, pretty_print=True, method='xml'))


input_path = 'beautiful_soup/testing_html.html'
output_path = 'beautiful_soup/xhtml_files/k.xhtml'
# Usage:
convert_html_to_xhtml(input_path, output_path)
