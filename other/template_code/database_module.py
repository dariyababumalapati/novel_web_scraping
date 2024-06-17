import os
import logging
import mysql.connector


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


def get_records(connection, sql_query):
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
        kgm_rows = cursor.fetchall()

        # Closing the cursor (optional, as the connection will be closed separately)
        cursor.close()

        return kgm_rows

    except mysql.connector.Error as error:
        print("Error fetching URLs: {}".format(error))
        return None

# Create a Table with required columns.

def get_records_by_id(connection, html_content, id):

    cursor = connection.cursor()

    # Update or insert data into kgm_html based on the fetched id
    update_query = f"UPDATE kgm_html SET raw_html = %s WHERE id = %s;"
    cursor.execute(update_query, (html_content, id))

    # Commit changes and close connection
    cursor.close()

import logging

def replace_words(connection, table, column, old_word, new_word):
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


def store_cleaned_html(connection, html_content_cleaned, id):
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


def store_xhtml(connection, xhtml_content, id):
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


if __name__ == '__main__':
    print('db_initiator.py is running in main.')

    db_connection = create_connection('novel_web_scraping')

    cursor = db_connection.cursor()

        # Retrieve data from the database
    cursor.execute("SELECT command_category, command, command_description FROM commands")

    print(cursor.fetchall()[0])


    cursor.close()
    db_connection.close()