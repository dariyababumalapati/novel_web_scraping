from txt_to_epub import txt_to_epub
from share_file.g_drive_upolad import upload_f_to_g_drive


chapter_number = 900

up_file_path = rf"C:\Users\91833\OneDrive\Desktop\books\ree\update\ree_{chapter_number}.txt"


txt_to_epub(up_file_path)

ree = "1AidBHDjC0QrafhxekBe5SFtqxJzL4Nli"
ra = "11cOTl6N5m9whAcPrQnCGksNRAE02GfGC"
file_name = rf"C:\Users\91833\Downloads\ree_{chapter_number}.epub"

upload_f_to_g_drive(file_name=file_name, folder_id=ree)