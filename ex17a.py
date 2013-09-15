from sys import argv
from os.path import exists

script, file1, file2 = argv

print "This program is going to copy stuf from the file1 to the file2"
	

inFile = open(file1)
data = inFile.read()

print "Does the second file exist? %r" % exists(file2)

outFile = open(file2, 'w')
outFile.write(data)

outFile.close()
inFile.close()

