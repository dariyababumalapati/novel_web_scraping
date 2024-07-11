import json
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def upload_f_to_g_drive(file_name, folder_id, folder_path=None):
    gauth = GoogleAuth()
    gauth.LoadClientConfigFile('share_file/client_secrets.json')

    credentials_file = "share_file/credentials.json"
    
    # Check if credentials file exists and load it
    if os.path.exists(credentials_file):
        gauth.LoadCredentialsFile(credentials_file)

    try:
        if gauth.credentials is None or gauth.access_token_expired:
            gauth.LocalWebserverAuth()
            gauth.SaveCredentialsFile(credentials_file)
        else:
            gauth.Authorize()
    except Exception as e:
        # Delete the corrupted credentials file and re-authenticate
        if os.path.exists(credentials_file):
            os.remove(credentials_file)
        print(f"Error during authentication, re-authenticating: {e}")
        gauth.LocalWebserverAuth()
        gauth.SaveCredentialsFile(credentials_file)

    drive = GoogleDrive(gauth)
    if folder_path:
        file_path = os.path.join(folder_path, file_name)
        file_title = file_name
    else:
        file_path = file_name
        file_title = os.path.basename(file_path)

    try:
        gfile = drive.CreateFile({'parents': [{'id': folder_id}], 'title': file_title})
        gfile.SetContentFile(file_path)
        gfile.Upload()
        print(f"File '{file_name}' uploaded successfully to Google Drive.")
    except Exception as e:
        print(f"Error uploading file: {e}")

if __name__ == "__main__":
    with open('inproject_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    start_number = 15
    stop_number = 50
    novel = 'fcse'

    file_name = fr"C:\Users\91833\Downloads\{novel}_{stop_number}.epub"
    
    drive_folders = {
        'novels': '1vb0JqLPHFNj9F4G7NRbgxI_Sips5GBVx',
        'hre': '1D31g6amVH_yiEuNkECC2sDGJJ81J2LhK',
        'mhag': "1ZusfIpX4bTnIRAxNpIABNhcMy54RFdCX",
        'ree': "1AidBHDjC0QrafhxekBe5SFtqxJzL4Nli",
        'lich': os.environ.get('LICH_NOVEL_FOLDER'),
        'fcse': '133H_cn0urMFlVOh-iSeShe_6wwVNZrz2',
    }

    folder_id = drive_folders[novel]

    upload_f_to_g_drive(file_name, folder_id)
    print('Running files upload to drive main')
