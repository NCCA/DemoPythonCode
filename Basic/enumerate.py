#!/usr/bin/python

colours=['red','green','blue','black','white']

c=list(enumerate(colours))
print c
c=list((enumerate(colours,start=2)))
print c

for i in range(0,len(colours)) :
	print i,colours[i]