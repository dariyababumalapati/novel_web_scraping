from database_module import create_connection, get_records

connection = create_connection('kgm')

query_all = "SELECT * FROM kgm_urls;"

records_all = get_records(connection, query_all)

url_all = [r[2] for r in records_all]

def cn():
    query = "SELECT * FROM kgm_html WHERE cleaned_html LIKE '%。%'"
    rows = get_records(connection, query)
    cn_li = [row[0] for row in rows]

    return cn_li

# print(r_li)

flag = True
cn_li = cn()
print(cn_li)

# while flag:
#     cn_li = cn()
#     print()
    
#     if not cn_li:
#         break


    