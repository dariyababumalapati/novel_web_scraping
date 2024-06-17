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


# creating a connection object to be used throughout the functions in the module.
connection = create_connection("kgm")


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

        # fetching all the urls returned by the query
        records = cursor.fetchall()

        # closing the cursor (optional, as the connection will be closed separately)
        cursor.close()

        return records

    except mysql.connector.error as error:
        print("error fetching urls: {}".format(error))
        return none


def set_column_by_id(column, html_content, chapter_id):
    try:
        cursor = connection.cursor()

        # update or insert data into kgm_html based on the fetched id
        update_query = f"update kgm_html set {column} = %s where id = %s;"
        cursor.execute(update_query, (html_content, chapter_id))

        # commit changes and close connection
        cursor.close()

    except mysql.connector.error as error:
        print("error setting_data: {}".format(error))
        return none


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
        update kgm_html
        set {column} = replace({column}, %s, %s)
        where {column} like concat('%', %s, '%');
        """

        cursor.execute(update_query, (old_word, new_word, old_word))
        connection.commit()
        cursor.close()
        logging.info(f"words replaced in {column} column of kgm_html table.")

    except exception as e:
        logging.error(f"error replacing words: {e}")


def check_raw_html(chapter_id):
    query = f"select raw_html from kgm_html where id={chapter_id}"
    html = get_records(connection, query)[0][0]
    create_html_file(html, "rw_html.html")

    connection.commit()


def get_cn_records_id():
    query = "select * from kgm_html where cleaned_html like '%。%'"
    rows = get_records(query)
    cn_li = [row[0] for row in rows]

    return cn_li


def get_cn_records():
    query = "select * from kgm_html where cleaned_html like '%。%'"
    rows = get_records(query)

    return rows


if __name__ == "__main__":
    print("db_initiator.py is running in main.")

    db_connection = create_connection("novel_web_scraping")

    cursor = db_connection.cursor()

    # retrieve data from the database
    cursor.execute(
        "select command_category, command, command_description from commands"
    )

    print(cursor.fetchall()[0])

    cursor.close()
    db_connection.close()
