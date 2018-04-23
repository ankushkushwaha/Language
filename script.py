#!/usr/bin/env python

# To run the script put 'python ./script.py' in terminal

file = open("sv_en","r")

lines = file.readlines()
file.close()
lines = [line.rstrip('\n') for line in open('sv_en')]

svArray = []
enArray = []

for s in lines:
	first,second = s.split(' = ')
	svArray.append( first );
	enArray.append( second );

thefile = open('en', 'w')
for item in enArray:
  print>>thefile, item+" = "

thefile.close()

thefile = open('sv', 'w')
for item in svArray:
  print>>thefile, item

thefile.close()

thefile = open('sv_en_backup', 'w')
for item in lines:
  print>>thefile, item

thefile.close()
