#!/usr/bin/python
from turtle import *


def Square(_size=20) :
	forward(_size)
	left(90)
	forward(_size)
	left(90)
	forward(_size)
	left(90)
	forward(_size)


penup()
goto(10,20)
pendown()
# comment
"""
this is a big comment

"""
Square(10)

penup()
goto(50,200)
pendown()
Square(100)

penup()
goto(300,100)
pendown()
Square(200)


done()




