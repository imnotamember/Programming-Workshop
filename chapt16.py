from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
# Sidenote: this exits badly by producing an error. How could we better handle this?
# print "If you don't want that, type 'Q'."
print "If you do want that, hit RETURN."

response = raw_input("?")

"""
if response == 'Q':
    quit()
"""

print "Opening the file..."

target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("%s\n%s\n%s\n" % (line1, line2, line3))
"""
#Alternative # 2: you could store the string to a variable like this:
what_to_write = line1 + "\n" + line2 + "\n" + line3 + "\n"
target.write(what_to_write)
"""

print "And finally, we close it."

target.close()

readit = open(filename)

print readit.read()

readit.close()
