import os
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


if __name__ == '__main__':
    print('db_initiator.py is running in main.')

    db_connection = create_connection('novel_web_scraping')

    cursor = db_connection.cursor()

        # Retrieve data from the database
    cursor.execute("SELECT command_category, command, command_description FROM commands")

    print(cursor.fetchall()[0])


    cursor.close()
    db_connection.close()