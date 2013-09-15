from sys import argv
from os.path import exists

script, a, b = argv

print "This app will magically copy stuff fro a to b"
print "Do you want to do that? yws - Return; no - CTRL-D"
raw_input('?')

aOpened = open(a)
aData = aOpened.read()

print "Let me check if your 2nd file exists %r" % exists(a)

bOpened = open(b, 'w')
bOpened.write(aData)

aOpened.close()
bOpened.close()

print "Thanks, all done"
