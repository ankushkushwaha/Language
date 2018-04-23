#!/usr/bin/env python

# To run the script put 'python ./script.py' in terminal

lines = [line.rstrip('\n') for line in open('en')]

svArray = []
enArray = []

for s in lines:
	first,second = s.split(' = ')
	enArray.append( first );
	if not second:
		svArray.append( "NOT ANSWERED" );
	else:
		svArray.append( second );

# print(svArray)

lines = [line.rstrip('\n') for line in open('sv_en')]

correct_sv_Array = []
correct_en_Array = []

for s in lines:
	first,second = s.split(' = ')
	correct_sv_Array.append( first );
	correct_en_Array.append( second );

index = 0
result = []

for correctString in correct_sv_Array:
	if correctString == svArray[index]:
		result.append("Correct : " + correctString);
		print(result[index])

	else:
		result.append("InCorrect:--------------------" + correctString + " : Your Answer: "+svArray[index]);
		print(result[index])

	index = index+1


thefile = open('autocheck', 'w')
for item in result:
 print>>thefile, item

thefile.close()