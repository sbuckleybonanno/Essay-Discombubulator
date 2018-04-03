import re
import nltk
import requests

class Essay(object):
	def __init__(self, text_filename, api_key_filename):
		with open(text_filename) as f:
			self.text = f.read()
		with open(api_key_filename) as f:
			self.api_key = f.read()
		self.split_text = re.findall("[a-zA-Z]+", self.text)
		
	
	def discombobulate(self):
		seen = set()
		seen_add = seen.add
		words = [x for x in self.split_text if not (x in seen or seen_add(x))] 
		for word in words:
			r = requests.get("http://words.bighugelabs.com/api/2/{0}/{1}/json".format(self.api_key, word))		
			data = r.json()
			print(data)
			return

