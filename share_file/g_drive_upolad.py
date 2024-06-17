import json
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def upload_f_to_g_drive(file_name, folder_id, folder_path=None,):
    gauth = GoogleAuth()
    gauth.LoadClientConfigFile('share_file/client_secrets.json')

    if os.path.exists("share_file/credentials.json"):
        gauth.LoadCredentialsFile("share_file/credentials.json")
        
    if gauth.credentials is None or gauth.access_token_expired:
        gauth.LocalWebserverAuth()
        gauth.SaveCredentialsFile("share_file/credentials.json")
    else:
        gauth.Authorize()

    drive = GoogleDrive(gauth)
    if folder_path:
        file_path = os.path.join(folder_path, file_name)
        file_title = file_name
    else:
        file_path = file_name
        file_title = os.path.basename(file_path)

    gfile = drive.CreateFile({'parents': [{'id': folder_id}], 'title': file_title})
    gfile.SetContentFile(file_path)
    gfile.Upload()
    print(f"File '{file_name}' uploaded successfully to Google Drive.")

if __name__ == "__main__":

    with open('inproject_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # chapters_range = data['chapters_range']

    start_number = 15

    stop_number = 50

    novel = 'fcse'
    
    dowloads_f_path = "C:/Users/91833/OneDrive/Desktop/books"
    file_name = fr"C:\Users\91833\Downloads\{novel}_{stop_number}.epub"
    generic_file_name = r"C:/Users/91833/OneDrive/Desktop/books/ree.epub"
    
    drive_folders ={
        'novels': '1vb0JqLPHFNj9F4G7NRbgxI_Sips5GBVx',
        'hre': '1D31g6amVH_yiEuNkECC2sDGJJ81J2LhK',
        'mhag': "1ZusfIpX4bTnIRAxNpIABNhcMy54RFdCX",
        'ree': "1AidBHDjC0QrafhxekBe5SFtqxJzL4Nli",
        'lich': os.environ.get('LICH_NOVEL_FOLDER'),
        'fcse': '133H_cn0urMFlVOh-iSeShe_6wwVNZrz2',

        }

    folder_id = drive_folders['fcse']

    upload_f_to_g_drive(file_name, folder_id)
    print('running files upload to drive main')