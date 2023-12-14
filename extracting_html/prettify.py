from bs4 import BeautifulSoup

num = 1159

# input_file = f'html_files/raw/{num}_raw.html'
# output_file = f'html_files/pretty/{num}_pretty.html'

input_file = 'extracting_html/non_chapter.html'
output_file = 'extracting_html/non_chapter_pretty.html'

with open(input_file, 'r', encoding='utf-8') as file:
    content = BeautifulSoup(file, 'html.parser')

formatted_html = content.prettify()

with open(output_file, 'w', encoding='utf-8') as file:
    file.write(formatted_html)
          
