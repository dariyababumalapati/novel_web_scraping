from bs4 import BeautifulSoup

from other.beautifulsoup_editing_modules import remove_elements, create_html_file

num = 1159

input_file = f'html_files/raw/{num}_raw.html'
output_file = f'html_files/pretty/{num}_pretty.html'

input_file = 'extracting_htmls/865_raw.html'
output_file = 'extracting_htmls/865_pretty.html'

with open(input_file, 'r', encoding='utf-8') as file:
    content = BeautifulSoup(file, 'html.parser')
    # content = remove_elements(file)

# chapter_title = create_html_file(content)
# print(chapter_title)
# print('ok')

formatted_html = content.prettify()

with open(output_file, 'w', encoding='utf-8') as file:
    file.write(formatted_html)
          
