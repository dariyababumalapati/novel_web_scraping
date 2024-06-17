import os
from bs4 import BeautifulSoup
import mysql.connector

with open('table_index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Establish a connection to your MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password=os.environ.get('MYSQL_PASSWORD'),
    database='novel_web_scraping'
    )

# Create a cursor to execute SQL queries
cursor = connection.cursor()

# Create a table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS chapters_index (
        chapter_number INT,
        url VARCHAR(255)
    )
''')

# Extract URLs and chapter numbers and insert them into the table
specific_ul = soup.find('div', class_='catalog', id='catalog').find('ul')

# print(specific_ul)

with open('url_list.html', 'w', encoding='utf-8') as f:
    f.write(specific_ul.prettify())

for li in specific_ul.find_all('li'):
    chapter_number = li.get('data-num')
    url = li.a.get('href')
    
    cursor.execute('''
        INSERT INTO chapters_index (chapter_number, url) VALUES (%s, %s)
    ''', (chapter_number, url))

# Commit changes and close the connection
connection.commit()
connection.close()
    