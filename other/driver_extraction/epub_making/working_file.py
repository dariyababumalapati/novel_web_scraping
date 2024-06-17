import json

from epub_maker import EpubMaker

with open('inproject_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# chapters_range = data['chapters_range']

# chapters_range = '21'



book_information = {
    "book_title": "KGM",
    "author_name": "niu",
    "language": "en",
    "image_file_path": "kgm.jpg",
    "folder_path": "files/xhtml_files_temp/mhag",
    "epub_file_name": "king_of_mercenaries",
    "destination_directory": "C:/Users/91833/OneDrive/Desktop/books/MHAG",
    }

king_of_gods = EpubMaker()
king_of_gods.make_epub(book_information)