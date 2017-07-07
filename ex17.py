from sys import argv
from os.path import exists

script, in_file, out_file = argv

print "Reading input file..."
inFile = open(in_file)
indata = inFile.read()

print "Length of input file is %d" % len(indata)

print "Does output file exist ? %r" % exists(out_file)

print "Writing to output file..."
outFile = open(out_file, "w")
outFile.write(indata)

inFile.close()
outFile.close()
