import os 

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = '1D31g6amVH_yiEuNkECC2sDGJJ81J2LhK'

directory = 'G:/Projects/Python_projects/novel_web_scraping/text_files/send_texts'

for f in os.listdir(directory):
    filename = os.path.join(directory, f)
    gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : f})
    gfile.SetContentFile(filename)
    gfile.Upload()