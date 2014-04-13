#Title: sample configuration
#Desc: use this as a template to create your own config file with the name of customConfig.py
#Author: Ricky Hewitt
#Created Date: 3/29/14


#import config class
import config

#set vars for config
#===============================================
#This message is outputted during scan.py to ensure you are using the correct conifg
message 	= 'Using Sample Config. The script will fail when posting to the endpoint. \nRefer to the README file to set a custom config.' 
#Any http(s):// endpoint such as http://requestb.in/
endpoint 	= 'http://www.sampleEndPoint.com/'
#Directory that script will scan. This should be a full directory E.g. /home/user/Documents/music
directory 	= '/home/user/sampleMusicDir' 






#instantiate config class
config = config.config()

#set config vars using above vars
config.set(message, endpoint, directory) 
