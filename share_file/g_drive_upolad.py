import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def upload_f_to_g_drive(folder_path, file_name, folder_id):
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

    file_path = os.path.join(folder_path, file_name)


    gfile = drive.CreateFile({'parents': [{'id': folder_id}], 'title': file_name})
    gfile.SetContentFile(file_path)
    gfile.Upload()
    print(f"File '{file_name}' uploaded successfully to Google Drive.")

if __name__ == "__main__":
    folder_id = '1D31g6amVH_yiEuNkECC2sDGJJ81J2LhK'
    print('running files upload to drive main')