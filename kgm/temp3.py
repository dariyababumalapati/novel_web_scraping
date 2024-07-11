from database_module import create_connection, check_raw_html, get_records


<<<<<<< HEAD
connection = create_connection("kgm")
=======
connection = create_connection('kgm')
>>>>>>> 0f6c9b9 (extraction complete)

query = "SELECT * FROM kgm_html WHERE cleaned_html LIKE '%%'"

rows = get_records(connection, query)

r_li = [row[0] for row in rows]

print(r_li)

# id = 6

# check_raw_html(connection, id)

connection.commit()
<<<<<<< HEAD
connection.close()
=======
connection.close()
>>>>>>> 0f6c9b9 (extraction complete)
