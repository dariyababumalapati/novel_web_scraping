from modules_ree.database_module_ree import get_records

query = 'select * from ree_htmls;'

raw_records = get_records(query)

for record in raw_records[:1]:
    chapter_id = record[0]
    raw_html = record[2]
    