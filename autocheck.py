#!/usr/bin/env python

# To run the script put 'python ./script.py' in terminal

lines = [line.rstrip('\n') for line in open('en.txt')]

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

lines = [line.rstrip('\n') for line in open('sv_en.txt')]

correct_sv_Array = []
correct_en_Array = []

for s in lines:
	first,second = s.split(' = ')
	correct_sv_Array.append( first );
	correct_en_Array.append( second );

index = 0
result = []
incorrectWords_Sv = []
incorrectWords_En = []

for correctString in correct_sv_Array:
	if correctString == svArray[index]:
		result.append("Correct : " + correctString);
	else:
		result.append("InCorrect:--------------------" + correctString + " : Your Answer: "+svArray[index]);
		incorrectWords_Sv.append( correctString );
		incorrectWords_En.append( correct_en_Array[index] );
	
	print("%d : %s" % (index+1, result[index]))
	index = index+1

print("%d : %d correct" % (len(incorrectWords_Sv), len(correct_sv_Array)))

# for incorrectWord in incorrectWords_Sv:
# 	print(incorrectWord)
		
print("InCorrect English words:--------------------")


for incorrectWord in incorrectWords_En:
		print(incorrectWord)

thefile = open('autocheck.txt', 'w')
for item in result:
 print>>thefile, item

thefile.close()
