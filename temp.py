import pyperclip

p = pyperclip.paste()

lines_li = p.split('\n')

del lines_li[:4]
# print(p)

print(lines_li[0])

# file_path = 'text_files/paste.txt'

# with open(file_path, 'w', encoding='utf-8') as file:
#     file.write()