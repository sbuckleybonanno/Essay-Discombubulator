import re

class Essay(object):
	def __init__(self, text, api_key):
		self.text = text
		self.api_key = api_key
		self.words = re.findall("[a-zA-Z]+", self.text)
	def discombobulate(self):
		 
		
