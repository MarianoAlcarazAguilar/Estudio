#! /home/user/anaconda3/bin/python

import string
letters = string.ascii_letters

for i in range(1,26):
	print(i, letters[:i] + letters[::-1][26-i:26])

