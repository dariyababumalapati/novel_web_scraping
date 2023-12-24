from bs4 import BeautifulSoup
import mysql.connector



# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Establish a connection to your MySQL database
connection = mysql.connector.connect(
    host='your_host',
    user='your_username',
    password='your_password',
    database='your_database'
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
for li in soup.find_all('li'):
    chapter_number = li.get('data-num')
    url = li.a.get('href')
    
    cursor.execute('''
        INSERT INTO chapters_index (chapter_number, url) VALUES (%s, %s)
    ''', (chapter_number, url))

# Commit changes and close the connection
connection.commit()
connection.close()
