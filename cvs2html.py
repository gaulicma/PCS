def readFile(Products):
	#read a fie and return a list
	with open(Products, 'r') as inFile:
		reader = csv.reader(inFile)
		aList = [row for now in reader]
	return aList

