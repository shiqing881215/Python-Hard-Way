from sys import argv

script, user_name = argv
prompt = '< '

print "Hi %s, I'm %s script" %(user_name, script)
print "I would like to ask you a few question"
print "Do you like me ?"
likes = raw_input(prompt)

print "Where do you live ?"
lives = raw_input(prompt)

print """
You said %r about liking me.
You live in %r.
""" %(likes, lives)
