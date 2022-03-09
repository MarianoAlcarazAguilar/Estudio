#! /home/user/anaconda3/bin/python

import os
import re
from functools import reduce

class TextCompare:

	def __init__(self, home_dir='.'):
		self.home_dir = home_dir
		self.collection = {}
		self.n_paragraphs = {}

	def list_files(self, file_path='.'):
		print(os.listdir(self.home_dir))

	def read_file(self, file_name):
		parsed_name = re.sub(r'\.[^\.]+$', '', file_name)
		with open(os.path.join(self, home_dir, file_name)) as f:
			self.collection[parsed_name] = f.read()
	
	def get_paragraphs(self, file_name):
		self.n_paragraphs[file_name] = len(self.collection[file_name].split('\n\n'))
		
	def get_mean_length_sentence ():
		
			
	
		

if __name__ == '__main__':

	tc1 = TextCompare('.')
	tc1.list_files()
	tc1.read_file('crime_text.txt')

