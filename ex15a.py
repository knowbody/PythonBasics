print "Hi there give me your filename:"

filename = raw_input("> ")
txt = open(filename)
print txt.read()
txt.close()
