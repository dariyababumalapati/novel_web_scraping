from database_module_kgm import get_records, create_connection

from beautifulsoup_module_kgm import create_html_file

connection = create_connection('kgm')

query = "SELECT * FROM kgm_html;"

rows = get_records(query)

raw_html = rows[10][2]

# with open('wild_raw.html', 'w', encoding='utf-8') as f:
#     f.write(raw_html)

create_html_file(raw_html, 'example_raw_html.html')