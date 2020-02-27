import os
from ftplib import FTP   

#FTP Settings
ftpUser = ''
ftpPass = ''
ftpAddress = 'speedtest.tele2.net'

#Folder settings
source_path = os.getcwd() + '/input/'
destination_path = os.getcwd() + '/output/'

print(source_path)

# Get a list of all files ending in .XML in source directory
included_extensions = ['xml','XML']
file_names = [fn for fn in os.listdir(source_path)
              if any(fn.endswith(ext) for ext in included_extensions)]


# initialise the FTP client
try:
   ftp = FTP(ftpAddress)   
   ftp.login(ftpUser,ftpPass) 
except Exception as e: 
    print('unable to connect to ftp server, aborting')
    print(e)
    quit()

# loop through all these files
for fname in file_names:
   print (source_path + fname)
  
   # send the file via ftp
   ftp.storlines('STOR ' + fname, open(source_path + fname,'r')) 
 
   # list files in ftp current directory
   #ftp.retrlines('LIST')

   # Move file to output directory
   os.rename(source_path + fname, destination_path + fname)
               
ftp.quit()   
