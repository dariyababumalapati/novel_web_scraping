from pydrive.drive import GoogleDrive 
from pydrive.auth import GoogleAuth 
import os 

# For using listdir() 
gauth = GoogleAuth() 
gauth.LocalWebserverAuth() 
drive = GoogleDrive(gauth) 

# replace the value of this variable with the absolute path of the directory 
path = r"C:\Games\Battlefield" 

# iterating through all the files/folder of the desired directory 
for x in os.listdir(path): 
   f = drive.CreateFile({'title': x}) 
   f.SetContentFile(os.path.join(path, x)) 
   f.Upload() 

   # Due to a known bug in pydrive if we don't empty the variable used to upload the files to Google Drive the file stays open in memory and causes a memory leak, therefore preventing its deletion 
   f = None