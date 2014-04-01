#Title: config
#Desc: base config class
#Author: Ricky Hewitt
#Created Date: 3/29/14

class config:
	def __init__(self):
		self.msg = ''
		self.endp = ''
		self.dir = ''

	def set(self, m, e, directory):
		self.msg = m
		self.endp = e
		self.dir = directory


