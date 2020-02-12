#!/usr/bin/env python
import string
import random
import sys

def password_gen():
	data = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	ret = ""
	for x in range(4):
		for y in range(3):
			ret = ret + random.choice(data)
		if x<3:
			ret = ret+"-"
	return ret


if len(sys.argv) == 1:
	print password_gen()
else:
	for x in range(int(sys.argv[1])):
		print password_gen()
