from sys import argv

script, filename = argv
# This will return you a file object
txt = open(filename)

print "Here is your file %s" % filename
print txt.read()

print "Type your filename again"
filename = raw_input("< ")

txt_again = open(filename)
print txt_again.read()
