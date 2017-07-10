from sys import argv

def split(stuff) :
	return stuff.split(" ")

def sort(words) :
	return sorted(words)

def first(words) :
	return words.pop(0)

def last(words) :
	return words.pop(-1)

def sort_sentence(sentence) :
	return sort(split(sentence))

def print_first_and_last(sentence) :
	words = split(sentence)
    #print words
	print first(words)
	print last(words)

def print_first_and_last_sorted(sentence) :
	words = sort_sentence(sentence)
	print first(words)
	print last(words)

print "The test string is \"Kobe Bryant is my favorite NBA player ever\" "
sentence = "Kobe Bryant is my favorite NBA player ever"

print_first_and_last(sentence)
print_first_and_last_sorted(sentence)
