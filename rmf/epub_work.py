from epub_maker import EpubMaker
import json

# Read the JSON file
with open('rmf/rmf_xhtml.json', 'r', encoding='utf-8') as file:
    xhtml_directory = json.load(file)


book_information = {
    "book_title": "RMF",
    "author_name": "Chen Rui",
    "language": "en",
    "image_file_path": "rmf.jpg",
    "folder_path": xhtml_directory,
    "epub_file_name": "rome_must_fall",
    "destination_directory": "C:/Users/91833/OneDrive/Desktop/books",
    }

king_of_gods = EpubMaker()
king_of_gods.make_epub(book_information)