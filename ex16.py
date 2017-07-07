from sys import argv

script, filename = argv

print "Erasing %r" % filename
print "If you care about the file, hit CTRL-C"
print "If you do want, hit ENTER"

raw_input("?")

print "Operning the file..."
target = open(filename, "w")

print "Truncating the file..."
target.truncate()

print "I'm going to ask for 3 lines..."

line1 = raw_input("Please enter the first line")
line2 = raw_input("Please enter the second line")
line3 = raw_input("Please enter the third line")

print "I'm going to write the file..."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print "Closing the file..."
target.close()
