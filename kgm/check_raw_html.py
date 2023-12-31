from database_module import get_records, create_connection

from beautifulsoup_module_kgm import create_html_file

connection = create_connection('kgm')

query = "SELECT * FROM kgm_html;"

rows = get_records(connection, query)

raw_html = rows[0][2]

create_html_file(raw_html, 'example_raw_html.html')