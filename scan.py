#Title: Scan  & FTP
#Desc: Scans & FTP file over to webserver
#Author: Ricky Hewitt
#Created Date: 12/27/13


#include libraries
import os
from ftplib import FTP
import time


#for url
import urllib.request
import urllib.parse
#set up initial music list to hold all files & folders names in directory
#musicList = []
#directory = 'FLACMusicLibrary/' # set up directory to scan

#walk through directory structure
#from os.path import join, getsize
#for root, dirs, files in os.walk(directory):
    #print(root, "consumes", end=" ")
#    if(root[17:] != ''):#remove the initial 'Music/'
#        musicList.append(root[17:])
    #print(sum(getsize(join(root, name)) for name in files), end=" ")
    #print("bytes in", len(files), "non-directory files")
    #if 'CVS' in dirs:
        #dirs.remove('CVS')  # don't visit CVS directories
        
        

host = 'hosthere'
username = 'usernamehere'
password = 'yourpasswordhere'

#print(musicList)
filename = 'Music.txt'


#write data to file
#file = open('Music.txt', 'w+')
#for music in musicList:
#    file.write(music+'\n')

#file.close()
enc="ISO-8859-1"
localfile = open('Music.txt', 'r', encoding=enc)
#print(localfile)
musicData = {}
artist = '';
for line in localfile:
    #if "\\" not in line:
     #   artist = line
    #else:
    #    album = line.rstrip('\n').split("\\")
        #musicData[artist][album[1].rstrip('\n')] = album[1]
    musicData[line] = line


    #test[line] = line

print(musicData);

#data = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
data = urllib.parse.urlencode(musicData)
data = data.encode('utf-8')
print(data);
request = urllib.request.Request("http://rphdev.no-ip.org/projects/home/musicCat/")
# adding charset parameter to the Content-Type header.
request.add_header("Content-Type","application/x-www-form-urlencoded;charset=utf-8")

f = urllib.request.urlopen(request, data)
print(f.read().decode('utf-8'))




#ftp file to webserver for consumption
#ftp = FTP(host) # connect to host webdev (local)
#ftp.login(username, password)
#print(ftp.getwelcome())
#ftp.cwd('projects/home/musicCat/data')


#ftp.retrbinary("RETR Music.txt", localfile.write)
#ftp.storlines("STOR Music.txt", open('Music.txt'))
#ftp.storbinary("STOR Music.txt", localfile.write)
#ftp.storbinary("STOR Music.txt", file(file, "rb"))
#ftp.storbinary('STOR' + localfile.name, open(file.name, 'wb').write)
#ftp.storlines("STOR Music.txt", open(localfile, 'r'))
#ftp.storlines('STOR Music.txt', file)
#ftp.sendcmd("chmod 777 'Music.txt'")
#print(ftp.retrlines('LIST'))
#ftp.quit()

