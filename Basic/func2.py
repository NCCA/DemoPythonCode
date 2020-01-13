#!/usr/bin/python
from __future__ import print_function 


def function1(data) :
	print('function 1 called with {}'.format(data))

def function2(data) :
	print('function 2 called with {}'.format(data))


functions=[function1,function2]

functions[0](12)
functions[1](12)
functions[0](99)
functions[1](88)






