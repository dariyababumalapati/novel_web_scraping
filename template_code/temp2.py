# UPDATE kgm_html
# SET my_column = REPLACE(raw_html, 'old_word', 'new_word')
# WHERE my_column LIKE '%old_word%';

# from helper_functions import create_file 
from beautifulsoup_module import create_html_file
from database_module import create_connection, get_records, replace_words

connection = create_connection('kgm')
table = 'kgm_html'
column = 'raw_html'

r_dict = {
    '’' : "'",
    '”' : "'",
    'Maximilian I' : 'Maximilian 1st',
    'Graubünden' : 'Graubunden',
    '…' : '..',
    'ｗ' : 'w',
    'UU Reading' : '',
    'www.uukansshu.net' : '',
    }

fullwidth_to_ascii = {
    'Ａ': 'A', 'Ｂ': 'B', 'Ｃ': 'C', 'Ｄ': 'D', 'Ｅ': 'E', 'Ｆ': 'F', 'Ｇ': 'G', 'Ｈ': 'H', 'Ｉ': 'I', 'Ｊ': 'J',
    'Ｋ': 'K', 'Ｌ': 'L', 'Ｍ': 'M', 'Ｎ': 'N', 'Ｏ': 'O', 'Ｐ': 'P', 'Ｑ': 'Q', 'Ｒ': 'R', 'Ｓ': 'S', 'Ｔ': 'T',
    'Ｕ': 'U', 'Ｖ': 'V', 'Ｗ': 'W', 'Ｘ': 'X', 'Ｙ': 'Y', 'Ｚ': 'Z', 'ａ': 'a', 'ｂ': 'b', 'ｃ': 'c', 'ｄ': 'd',
    'ｅ': 'e', 'ｆ': 'f', 'ｇ': 'g', 'ｈ': 'h', 'ｉ': 'i', 'ｊ': 'j', 'ｋ': 'k', 'ｌ': 'l', 'ｍ': 'm', 'ｎ': 'n',
    'ｏ': 'o', 'ｐ': 'p', 'ｑ': 'q', 'ｒ': 'r', 'ｓ': 's', 'ｔ': 't', 'ｕ': 'u', 'ｖ': 'v', 'ｗ': 'w', 'ｘ': 'x',
    'ｙ': 'y', 'ｚ': 'z'
}


for key, value in r_dict.items():
    replace_words(connection, table, column, key, value)

id = '30'
query = f'SELECT raw_html FROM kgm_html WHERE id={id}'
html = get_records(connection, query)[0][0]
create_html_file(html, 'rw_html.html')

# print(html)
connection.commit()
connection.close()