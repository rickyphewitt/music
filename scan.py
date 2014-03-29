#Title: Scan  & POST
#Desc: Scans & POST data to webserver
#Author: Ricky Hewitt
#Created Date: 12/27/13
#Updated Date: 3/29/14


#include libraries
import os
import time
import imp
import sys

#for post
import urllib.request
import urllib.parse

#import needed class files

#include config file
#check for custom config file first
#fall back on sample config
#set config to a short var for ease of use
try:
	imp.find_module('configs')
	import config
	con = config.config
except ImportError:
	import sampleConfig
	con = sampleConfig.config


import buildMusic
music = buildMusic.music()
#music.build(con.dir)

music = music.build(con.dir)

#output config message and endpoint
print(con.msg+'\n')
print('Current Endpoint '+con.endp+'\n')

enc="ISO-8859-1"
localfile = open('Music.txt', 'r', encoding=enc)
#print(localfile)

musicData = {}
artist = '';
print('Building POST data')
for line in localfile:
     musicData[line] = line

#data = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
print('Encoding POST data')
data = urllib.parse.urlencode(musicData)
data = data.encode('utf-8')

print('Setting Endpoint')
request = urllib.request.Request(con.endp)
# adding charset parameter to the Content-Type header.
print('Setting Header')
request.add_header("Content-Type","application/x-www-form-urlencoded;charset=utf-8")
print('Sending Request')
try:

    f = urllib.request.urlopen(request, data)
    print('Success!')
    print('Returned status')
    print(f.read().decode('utf-8'))

except: #currently catching all errors
    print('Failure!')
    print('Check your endpoint in the configuration')
    #print('Actual error: /n'+sys.exc_info()[0])




