#!/usr/bin/env python

# To run the script put 'python ./script.py' in terminal


lines = [line.rstrip('\n') for line in open('sv_en.txt')]

svArray = []
enArray = []

for s in lines:
	first,second = s.split(' = ')
	svArray.append( first );
	enArray.append( second );

thefile = open('en.txt', 'w')
for item in enArray:
  print>>thefile, item+" = "

thefile.close()

thefile = open('sv.txt', 'w')
for item in svArray:
  print>>thefile, item

thefile.close()

thefile = open('sv_en_backup', 'w')
for item in lines:
  print>>thefile, item

thefile.close()
