from epub_maker import EpubMaker



book_information = {
    "book_title": "MHAG 890-916",
    "author_name": "xi hanyue",
    "language": "en",
    "image_file_path": "cover.jpg",
    "folder_path": "files/xhtml_files_temp/mhag",
    "epub_file_name": "MHAG_894-916_cleaned",
    "destination_directory": "novels_scrapped_epub",
    }

king_of_gods = EpubMaker()
king_of_gods.make_epub(book_information)