from bs4 import BeautifulSoup

from modules_ree.database_module_ree import create_connection


def extract_urls(filepath: str):

    connection = create_connection('ree')
    cursor = connection.cursor() 
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    specific_ul = soup.find('ul', id='chapterList')
    print(len(specific_ul))
    chapters = []

    for li in specific_ul.find_all('li')[::-1]:
    
        try:
            chapter_title = li.a.get_text(strip=True)
            
            url_part = li.a.get('href')
            url = f"https://www.uukanshu.net/{url_part}"

            chapters.append((chapter_title, url))
        except:
            print('invalid li element')

    for chapter in chapters:

        # print(chapter_title)
        cursor.execute("""
            INSERT INTO ree_urls (chapter_title, url) VALUES (%s, %s)       
        """, chapter
        )

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':

    file_p = "ree/imp_files/url_page_ree.html"

    extract_urls(file_p)

