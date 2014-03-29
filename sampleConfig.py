#Title: sample configuration
#Desc: use this as a template to create your own config file
#Author: Ricky Hewitt
#Created Date: 3/29/14
#simple config class
class config:
	def __init__(self):
		self.msg = ''
		self.endp  = ''
		self.dir = ''

	def set(self, m, e, directory):
		self.msg = m
		self.endp = e
		self.dir = directory

config = config()
config.set('Using Sample Config. The script will fail when posting to the endpoint. \nRefer to the README file to set a custom config.', 'http://www.sampleEndPoint.com/', 'sampleDir') 
