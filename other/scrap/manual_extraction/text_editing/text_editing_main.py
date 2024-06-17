from useful_operations.name_the_file import name_the_file

from text_editing.useful_text_operations import remove_lines_with_prefixes, replace_words_in_file

from text_editing.line_editing import join_broken_lines, find_broken_lines




chap_num = 'novel_text'

file_p = f'text_files/{chap_num}.txt'
temp_p = f'text_files/temp_file.txt'
cleaned_file_p = f'text_files/chapters_cleaned/{chap_num}_cleaned.txt'
broken_file_p = f'text_files/broken_lines/{chap_num}_broken.txt'


prefixes_to_remove_list = ['2020-', 'Holy Roman Empire-', 'Close']
replacements = {
'China': 'Central',
'China-Europe': 'Central-Europe',
'China-EU': 'Central-EU',
"’": "'",
# Add more old_word: new_word pairs as needed
}


broken = False


remove_lines_with_prefixes(file_path_i=file_p, file_path_o=file_p, prefixes_to_remove=prefixes_to_remove_list)



join_broken_lines(file_path_i=file_p, file_path_o=cleaned_file_p)

if broken:
    find_broken_lines(file_path_i=temp_p, file_path_o=broken_file_p)

else:
    pass

replace_words_in_file(file_path=cleaned_file_p, replacement_words=replacements)


with open(temp_p, 'w') as file:
    pass

