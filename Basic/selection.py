#!/usr/bin/python

from turtle import *

type = "Triangle"

if type == "Square" :
	forward(100)
	left(90)
	forward(100)
	left(90)
	forward(100)
	left(90)
	forward(100)
	done()
	if type == "Square" :
		forward(100)
		left(90)
		forward(100)
		left(90)
		forward(100)
		left(90)
		forward(100)
		done()


elif type=="Triangle" :
	forward(100)
	right(120)
	forward(100)
	right(120)
	forward(100)
	done()

else :
	print "nothing selected"

