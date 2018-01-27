#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''import os

direc = os.getcwd() # Get current working directory
ext = '.png' # Select your file delimiter
arq = open('a.txt','wb')

file_dict = {} # Create an empty dict

# Select only files with the ext extension
txt_files = [i for i in os.listdir(direc) if os.path.splitext(i)[1] == ext]

# Iterate over your txt files
for f in txt_files:
    # Open them and assign them to file_dict
    with open(os.path.join(direc,f)) as file_object:
        file_dict[f[:-4]] = f

# Iterate over your dict and print the key/val pairs.
arq.write('palavras = {')
for i in file_dict:
    arq.write('\'')
    arq.write(str(file_dict[i][:-4]))
    arq.write('\'')
    arq.write(':')
    arq.write('\'')
    arq.write(str(file_dict[i]))
    arq.write('\'')
    arq.write(',')

arq.write('}')
arq.close()'''

import os

"""
Renames the filenames within the same directory to be Unix friendly
(1) Changes spaces to hyphens
(2) Makes lowercase (not a Unix requirement, just looks better ;)
Usage:
python rename.py
"""

path =  os.getcwd()
filenames = os.listdir(path)

for filename in filenames:
    os.rename(filename, filename.lower())