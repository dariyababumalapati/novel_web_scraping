from database_module import create_connection, check_raw_html, get_records


connection = create_connection("kgm")

query = "SELECT * FROM kgm_html WHERE cleaned_html LIKE '%%'"

rows = get_records(connection, query)

r_li = [row[0] for row in rows]

print(r_li)

# id = 6

# check_raw_html(connection, id)

connection.commit()
connection.close()
