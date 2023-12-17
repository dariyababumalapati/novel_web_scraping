from epub_maker import EpubMaker



book_information = {
    "book_title": "MHAG 917-936",
    "author_name": "Chen Rui",
    "language": "en",
    "image_file_path": "cover.jpg",
    "folder_path": "files/xhtml_files_temp/mhag",
    "epub_file_name": "MHAG_917-936",
    "destination_directory": "files/novels_scrapped_epub",
    }

king_of_gods = EpubMaker()
king_of_gods.make_epub(book_information)