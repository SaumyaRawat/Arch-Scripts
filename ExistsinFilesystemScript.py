#!/usr/bin/python

# This script deletes all files included as "so and so file exists in the filesystem" error. 
# Assumes the file has no spaces!
# Will ask for sudo password!

import re
import os

f = open('debug_input.txt','r') #open file containing lines as "filename exists in the system"
fOut = open('input.txt','w') # file will contain only to delete filenames

lines = f.readlines()
data_list = []
for line in lines:
	data_list.append(re.findall(r'\S+', line)[1])

for line in data_list:
	cmdstring = "sudo rm  %s" % (line)
	os.system(cmdstring)