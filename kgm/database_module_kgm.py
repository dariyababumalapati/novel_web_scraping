import os
import logging
import mysql.connector

from beautifulsoup_module_kgm import create_html_file

def create_connection(database_name: str):
    connection  = mysql.connector.connect(
        host='localhost',
        user='root',
        password=os.environ.get('MYSQL_PASSWORD'),
        database=database_name
        )

    if connection.is_connected():
        print('Connection is established.\n')
        
        return connection

    else:
        print('Connection failed.')


# creating a connection object to be used throughout the functions in the module.
connection = create_connection('kgm')


def get_records(sql_query):
    """Get the URL from the table in the database from the 'url' column.

    Args:
        connection (): database_connection
        prompt (string): the prompt for the database.
    """
    try:
        # Creating a cursor object using the connection
        cursor = connection.cursor()


        # Executing the SQL query
        cursor.execute(sql_query)

        # Fetching all the URLs returned by the query
        records = cursor.fetchall()

        # Closing the cursor (optional, as the connection will be closed separately)
        cursor.close()

        return records

    except mysql.connector.Error as error:
        print("Error fetching URLs: {}".format(error))
        return None


def set_column_by_id(column, html_content, chapter_id):

    try:
        cursor = connection.cursor()

        # Update or insert data into kgm_html based on the fetched id
        update_query = f"UPDATE kgm_html SET {column} = %s WHERE id = %s;"
        cursor.execute(update_query, (html_content, chapter_id))

        # Commit changes and close connection
        cursor.close()

    except mysql.connector.Error as error:
        print("Error setting_data: {}".format(error))
        return None

def replace_words(column, old_word, new_word):
    """
    Replace occurrences of a word in a specific column of a table in the database.

    Args:
    - connection: Database connection object.
    - table (str): Name of the table.
    - column (str): Name of the column to be updated.
    - old_word (str): Word to be replaced.
    - new_word (str): Replacement word.

    Returns:
    - None
    """
    try:
        cursor = connection.cursor()
        
        # Use parameterized queries to prevent SQL injection
        update_query = f"""
        UPDATE kgm_html
        SET {column} = REPLACE({column}, %s, %s)
        WHERE {column} LIKE CONCAT('%', %s, '%');
        """
        
        cursor.execute(update_query, (old_word, new_word, old_word))
        connection.commit()
        cursor.close()
        logging.info(f"Words replaced in {column} column of kgm_html table.")
    
    except Exception as e:
        logging.error(f"Error replacing words: {e}")


def check_raw_html(chapter_id):

    query = f'SELECT raw_html FROM kgm_html WHERE id={chapter_id}'
    html = get_records(connection, query)[0][0]
    create_html_file(html, 'rw_html.html')

    connection.commit()


def get_cn_records_id():
    query = "SELECT * FROM kgm_html WHERE cleaned_html LIKE '%。%'"
    rows = get_records(query)
    cn_li = [row[0] for row in rows]

    return cn_li

def get_cn_records():
    query = "SELECT * FROM kgm_html WHERE cleaned_html LIKE '%。%'"
    rows = get_records(query)

    return rows

if __name__ == '__main__':
    print('db_initiator.py is running in main.')

    db_connection = create_connection('novel_web_scraping')

    cursor = db_connection.cursor()

        # Retrieve data from the database
    cursor.execute("SELECT command_category, command, command_description FROM commands")

    print(cursor.fetchall()[0])


    cursor.close()
    db_connection.close()