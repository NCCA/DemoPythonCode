#!/usr/bin/python

from MyContainer import *

c=MyContainer([1,2,3,4,5,"string","c"])
print c
print "length of c is ",len(c)
c[2]="new value"
print "c[2] is ",c[2]
del c[2]
print "deleted item 2 ",c
print "using the iterator"
for i in c :
	print i

print "using reverse iterator"
for i in reversed(c) :
	print i

c.append(999)
print c
