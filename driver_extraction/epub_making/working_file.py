import json

from epub_maker import EpubMaker

with open('inproject_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

chapters_range = data['chapters_range']

book_information = {
    "book_title": "MHAG",
    "author_name": "Chen Rui",
    "language": "en",
    "image_file_path": "cover.jpg",
    "folder_path": "files/xhtml_files_temp/mhag",
    "epub_file_name": f"MHAG_{chapters_range}",
    "destination_directory": "C:/Users/91833/OneDrive/Desktop/books/MHAG",
    }

king_of_gods = EpubMaker()
king_of_gods.make_epub(book_information)