#Title: sample configuration
#Desc: use this as a template to create your own config file with the name of customConfig.py
#Author: Ricky Hewitt
#Created Date: 3/29/14


#import config class
import config

config = config.config()

config.set('Using Sample Config. The script will fail when posting to the endpoint. \nRefer to the README file to set a custom config.', 'http://www.sampleEndPoint.com/', 'sampleMusicDir') 
