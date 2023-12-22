

for file in 

html_content = copy_useful_html(driver=driver)
soup = remove_elements(html_content)
soup = remove_elements_with_certain_texts(soup, texts_to_remove=texts_to_remove_list)
soup = replace_words_in_html(soup, replace_words=replace_words_dict)
soup = replace_dots_with_dash(soup)
chapter_number = get_chapter_number(soup=soup)

file_path = f'files/html_files/mhag/chapter_{chapter_number}.html'
create_html_file(soup=soup, file_path=file_path)


input_file_path = file_path
output_file_path = f'files/xhtml_files/mhag/chapter_{chapter_number}.html'
output_file_path_temp = f'files/xhtml_files_temp/mhag/chapter_{chapter_number}.html'