#!/usr/bin/python
from __future__ import print_function

def multiReturn(_data) :
	a=_data*1
	b=_data*2
	c=_data*3
	return a,b,c


data=["test","values"]

x,y,z=multiReturn(data)
print( x )
print( y )
print( z )





