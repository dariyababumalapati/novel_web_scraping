import os

import pyperclip



p_c = pyperclip.paste()

chap_num = 10

filepath = f'ree_{chap_num}.txt'

print(filepath)
# for _ in range(3):
#     with open(filepath, 'a', encoding='utf-8') as f:
#         f.write(p_c)


# os.remove(filepath)