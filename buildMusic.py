#Title: build music
#Desc: Builds the list of artist/album data
#Author: Ricky Hewitt
#Created Date: 3/29/14
#Updated Date: 3/29/14

from os.path import join, getsize
import os

class music:
	def __init__(self):
		self.musicList = []
		self.file = open('Music.txt', 'r', encoding="ISO-8859-1")
	
	def build(self, directory):
        	#walk through directory structure 
        	#write data to file
        	#file = open('Music.txt', 'w+')
        	#for music in musicList:
        	#    file.write(music+'\n')

        	#file.close()
        	#print('@ToDo: uncomment build file')
        	print('')

	def get(self):
		return self.musicList

	def getFile(self):
        	print('within getFile')
        	#enc="ISO-8859-1"
        	#localfile = open('Music.txt', 'r', encoding=enc)
        	return self.file   



def readDir(directory, musicList): 
	for root, dirs, files in os.walk(directory):
		print(root, "consumes", end=" ")
		if(root[17:] != ''):#remove the initial 'Music/'
			musicList.append(root[17:])
			print(sum(getsize(join(root, name)) for name in files), end=" ")
			print("bytes in", len(files), "non-directory files")
		if 'CVS' in dirs:
			dirs.remove('CVS')  # don't visit CVS directories
	return musicList
