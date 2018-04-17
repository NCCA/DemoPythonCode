#!/usr/bin/python

from turtle import *

def Square(_size) :
	for i in range(0,4) :
		forward(_size)
		left(90)

for x in range(-250,250,40) :
	print x
	goto(x,0)
	Square(40)

done()
