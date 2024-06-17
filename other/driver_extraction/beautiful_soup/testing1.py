from bs4 import BeautifulSoup
import requests

number = '2'
url = f'https://www.ultrasmangateam.it/cinese/king-of-gods/kog-cap-{number}/'

HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

novel_chapter_page = requests.get(url, headers=HEADERS)
novel_chapter_page_doc = BeautifulSoup(novel_chapter_page.text, 'html.parser')

body = novel_chapter_page_doc.article

body.h1.string = f'Chapter {number}'
p_tag = body.p
p_tag.string = ''
body.h2.replace_with(p_tag)
[body.h3.decompose() for h3 in body.find_all('h3')]

formatted_html = body.prettify()

file_p = 'beautiful_soup/testing_html.html'

with open(file_p, 'w', encoding='utf-8') as file:
    file.write(formatted_html)