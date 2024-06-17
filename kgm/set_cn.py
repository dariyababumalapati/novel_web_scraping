from database_module_kgm import create_connection, get_records, get_cn_records, set_column_by_id

# from beautifulsoup_module import create_html_file, merge_elements, remove_elements_with_certain_texts, replace_words_in_html
from beautifulsoup_module_kgm import *

from helper_functions_kgm import delete_file

connection = create_connection('kgm')

query_html = 'SELECT * FROM kgm_html;'
html_rows = get_cn_records()

query_remove = 'SELECT remove_words FROM remove_text;'
rm_rows = get_records(query_remove)
rm_list = [row[0] for row in rm_rows]

query_replace = 'SELECT * FROM replace_text;'
rp_rows = get_records(query_replace)
rp_dict = {rp[1]: rp[2] for rp in rp_rows}

missing_chapters = []


for row in html_rows:
    chapter_id = row[0]
    html_content = row[2]

    try:
        soup = merge_elements(html_content)

        soup = remove_elements_with_certain_texts(soup, rm_list)

        html_cleaned = replace_words_in_html(soup, rp_dict)

        set_column_by_id('cleaned_html', html_cleaned, chapter_id)

        xhtml_content = convert_html_to_xhtml_kgm(html_cleaned)
        
        set_column_by_id('xhtml', xhtml_content, chapter_id)

    except:
        print(row[0])
        missing_chapters.append(row[0])


if missing_chapters:
    print(missing_chapters)
    # time.sleep(100)
else:
    print('No missing_chapters.')

connection.commit()
connection.close()

file_name = f"C:/Users/91833/OneDrive/Desktop/books/king_of_mercenaries.epub"
delete_file(file_name)


