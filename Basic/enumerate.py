#!/usr/bin/python
from __future__ import print_function
colours=['red','green','blue','black','white']

c=list(enumerate(colours))
print(c)
c=list((enumerate(colours,start=2)))
print(c)

for number,colour in enumerate(colours) :
	print (number,colour)
print("use _ to ignore a value")
for _,colour in enumerate(colours) :
	print (colour)