from epub_maker import EpubMaker



book_information = {
    "book_title": "MHAG 961-965",
    "author_name": "Chen Rui",
    "language": "en",
    "image_file_path": "cover.jpg",
    "folder_path": "files/xhtml_files_temp/mhag",
    "epub_file_name": "MHAG_961-965",
    "destination_directory": "C:/Users/91833/OneDrive/Desktop/books/MHAG",
    }

king_of_gods = EpubMaker()
king_of_gods.make_epub(book_information)