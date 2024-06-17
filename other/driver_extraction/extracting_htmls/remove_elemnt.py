from bs4 import BeautifulSoup

# HTML content (Replace this with your HTML content)
# html_content = '''
# <div>
#     <h1>Hello</h1>
#     <h1 class="hide720">World</h1>
#     <p>Some text</p>
# </div>
# '''
file_path = "extracting_html/1159_pretty.html"
file_path2 = "extracting_html/1159_pretty2.html"

with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()


# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find the element with class 'hide720'
# element_to_remove = soup.find('h1', class_='hide720')

# # Remove the element if found
# if element_to_remove:
#     element_to_remove.extract()

def remove_primary_three_elements():
    elements_to_remove = soup.find_all(lambda tag: tag.name == 'h1' and 'hide720' in tag.get('class', []) or 
                                                tag.name == 'div' and 'hide720' in tag.get('class', []) or
                                                tag.name == 'div' and tag.get('id') == 'txtright')

    for element in elements_to_remove:
        element.extract()

# Find the element with string '(End of chapter)'
end_of_chapter_element = soup.find(string=lambda text: text and '(End of chapter)' in text.strip())
print(end_of_chapter_element)

# Remove all elements after the end_of_chapter_element
if end_of_chapter_element:
    # Get the parent of the end_of_chapter_element
    grandparent = end_of_chapter_element.find_parent().find_parent()

    print(grandparent)
    
    # Extract the parent and all its siblings
    while grandparent.next_sibling:
        grandparent.next_sibling.extract()

with open(file_path2, 'w', encoding='utf-8') as file:
    file.write(soup.prettify())