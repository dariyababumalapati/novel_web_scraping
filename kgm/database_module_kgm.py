import os
import logging
import mysql.connector

from beautifulsoup_module_kgm import create_html_file


def create_connection(database_name: str):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.environ.get("mysql_password"),
        database=database_name,
    )

    if connection.is_connected():
        print("connection is established.\n")

        return connection

    else:
        print("connection failed.")

connection = create_connection('kgm')

def get_records(sql_query):
    """get the url from the table in the database from the 'url' column.

    args:
        connection (): database_connection
        prompt (string): the prompt for the database.
    """
    try:
        # creating a cursor object using the connection
        cursor = connection.cursor()

        # executing the sql query
        cursor.execute(sql_query)

        # Fetching all the URLs returned by the query
        kgm_rows = cursor.fetchall()

        # closing the cursor (optional, as the connection will be closed separately)
        cursor.close()

        return records

    except mysql.connector.error as error:
        print("error fetching urls: {}".format(error))
        return none


def set_column_by_id(column, html_content, id):

    cursor = connection.cursor()

    # Update or insert data into kgm_html based on the fetched id
    update_query = f"UPDATE kgm_html SET {column} = %s WHERE id = %s;"
    cursor.execute(update_query, (html_content, id))

    # Commit changes and close connection
    cursor.close()

import logging

def replace_words(column, old_word, new_word):
    """
    replace occurrences of a word in a specific column of a table in the database.

    args:
    - connection: database connection object.
    - table (str): name of the table.
    - column (str): name of the column to be updated.
    - old_word (str): word to be replaced.
    - new_word (str): replacement word.

    returns:
    - none
    """
    try:
        cursor = connection.cursor()

        # use parameterized queries to prevent sql injection
        update_query = f"""
        UPDATE {table}
        SET {column} = REPLACE({column}, %s, %s)
        WHERE {column} LIKE CONCAT('%', %s, '%');
        """

        cursor.execute(update_query, (old_word, new_word, old_word))
        connection.commit()
        cursor.close()
        logging.info(f"Words replaced in {column} column of {table} table.")
    
    except Exception as e:
        logging.error(f"Error replacing words: {e}")


def store_cleaned_html(html_content_cleaned, id):
    """
    Store HTML_cleaned content into the database.

    Args:
    - connection: Database connection object.
    - html_content_cleaned (str): HTML content to be stored.
    - id (int): id
    Returns:
    - None
    """
    try:
        cursor = connection.cursor()
        update_query = f"UPDATE kgm_html SET cleaned_html = %s WHERE id = %s;"
        cursor.execute(update_query, (html_content_cleaned, id))
        connection.commit()
        cursor.close()
        print("HTML_cleaned content stored successfully.")
    except Exception as e:
        print(f"Error storing HTML_cleaned content: {e}")


def store_xhtml(xhtml_content, id):
    """
    Store XHTML content into the database.

    Args:
    - connection: Database connection object.
    - xhtml_content (str): XHTML content to be stored.
    - id (int): id 

    Returns:
    - None
    """
    try:
        cursor = connection.cursor()
        update_query = f"UPDATE kgm_html SET xhtml = %s WHERE id = %s;"
        cursor.execute(update_query, (xhtml_content, id))
        connection.commit()
        cursor.close()
        print("XHTML content stored successfully.")
    except Exception as e:
        print(f"Error storing XHTML content: {e}")

def check_raw_html(id):

    query = f'SELECT raw_html FROM kgm_html WHERE id={id}'
    html = get_records(connection, query)[0][0]
    create_html_file(html, "rw_html.html")

    connection.commit()

def get_cn_records():
    query = "SELECT * FROM kgm_html WHERE cleaned_html LIKE '%。%'"
    rows = get_records(connection, query)
    cn_li = [row[0] for row in rows]

    return cn_li

if __name__ == '__main__':
    print('db_initiator.py is running in main.')

    db_connection = create_connection("novel_web_scraping")

    cursor = db_connection.cursor()

    # retrieve data from the database
    cursor.execute(
        "select command_category, command, command_description from commands"
    )

    print(cursor.fetchall()[0])

    cursor.close()
    db_connection.close()
