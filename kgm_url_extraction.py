from bs4 import BeautifulSoup

from database_actions_module.db_initiator import create_connection

data_base = 'novel_web_scraping'
connection = create_connection(data_base)
cursor = connection.cursor()

with open('kgm.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

specific_ul = soup.find('ul', id='chapterList')

# print(specific_ul)

chapters = []

for li in specific_ul.find_all('li')[::-1]:

    chapter_title = li.a.get_text(strip=True)
    
    url_part = li.a.get('href')
    url = f"https://www.uukanshu.net/{url_part}"

    chapters.append((chapter_title, url))

for chapter in chapters:

    # print(chapter_title)
    cursor.execute("""
        INSERT INTO kgm (chapter_title, url) VALUES (%s, %s)       
    """, chapter
    )

connection.commit()
cursor.close()
connection.close()