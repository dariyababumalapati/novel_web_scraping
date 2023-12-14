import os
numbe = ['1109', '1113']

file_path_cleaned = f'text_files/chapters_cleaned/{numbe[0]}-{numbe[1]}_cleaned.txt'
full_file_path = os.path.abspath(file_path_cleaned)
print(full_file_path)