import os

from share_file.g_drive_upolad import upload_f_to_g_drive

g_drive_folder_id = '1D31g6amVH_yiEuNkECC2sDGJJ81J2LhK'

chapter_indexes = ['1125', '1129']

dowloads_f_path = "C:/Users/91833/Downloads"

uplaod_file_name = f'{chapter_indexes[0]}-{chapter_indexes[-1]}_cleaned.epub'

upload_f_to_g_drive(folder_path=dowloads_f_path, file_name=uplaod_file_name, folder_id=g_drive_folder_id)