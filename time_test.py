file_path = 'chapter_title.txt'

chapter_title = 'ming 100'

chapter_content = 'this is the chapter content.'

with open(file_path, 'a', encoding='utf-8') as f:
    f.write(chapter_title)
    f.write(chapter_content)
