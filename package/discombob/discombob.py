import re

class Essay(object):
	def __init__(self, text_filename, api_key_filename):
		with open(text_filename) as f:
			self.text = f.read()
		with open(api_key_filename) as f:
			self.api_key = f.read()
		this.split_text = re.findall("[a-zA-Z]+", self.text)
		seen = set()
		seen_add = seen.add
		self.words = [x for x in this.split_text if not (x in seen or seen_add(x))]
	
	# def discombobulate(self):
		 
		
