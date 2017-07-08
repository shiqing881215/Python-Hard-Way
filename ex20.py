from sys import argv

script, filename = argv

def read_all(f) : 
	print f.read()

def rewind(f) : 
	f.seek(0)

def read_a_line(f) : 
	print f.readline()

file = open(filename)

print "First print out the whole file content"
read_all(file)

print "Rewind the file to the top"
rewind(file)

print "Print 2 lines of the file"
read_a_line(file)
read_a_line(file)

file.close()
