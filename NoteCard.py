# Script to replicate note cards
# values are delimited by a ","
# only put two values per line 
# representing both sides of a note card
# press q to exit program

#Example of file data entrys: 
#poeta -ae,poet
#bellum -a,war

from time import sleep

setValue = raw_input("Side 1 or 2?  \n")
fileLocation = raw_input("Enter source file location \n")

f = open(fileLocation, 'r')
setList = []

for line in f.readlines():
	line = line.strip('\n')
	lineList = line.split(',')
	setList.append((lineList[0], lineList[1]))


userInput = ""
index = 0

while userInput != "q":
	if setValue == 1:
		userInput = raw_input(setList[index][0])
		print setList[index][1]
	else:
		userInput = raw_input(setList[index][1])
		print setList[index][0]

	sleep(2)
	print ""
	index += 1
	if index == len(setList):
		index = 0
