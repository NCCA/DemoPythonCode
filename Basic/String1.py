#!/usr/bin/python

# declare a string

File = "Pass.0001.exr"

print File
print "The string has %d elements " %(len(File))

# we can treat a string like a list
for i in range(0,len(File)) :
	print File[i]
# we can find the index of a particular element
print File.find(".ex")
# we can split the string based on a character
StringList = File.split(".")
print StringList;
# we can replace elements
File=File.replace("Pass","BeautyPass")
print File
# see if file starts with a particular string
print File.startswith("BeautyPass")
# see if file ends with a particular string
print File.endswith(".exr")