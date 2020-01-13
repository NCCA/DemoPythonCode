#!/usr/bin/python
from __future__ import print_function

def defaultArguments( a, b=0, c=0, d=0) :
	print('a={} b={} c={} d={}'.format(a,b,c,d) )
	
defaultArguments(3)
defaultArguments(c=9,a=2)
defaultArguments(1,2,3,4)
defaultArguments()