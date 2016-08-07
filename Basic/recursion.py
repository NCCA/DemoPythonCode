#!/usr/bin/python
# code taken from http://docs.python.org/dev/library/turtle.html

import turtle
wn = turtle.Screen()
wn.setup(800,400)
turtle = turtle.Turtle()
turtle.speed(0)
def spiral(n):
    if n < 300:
        turtle.forward(n)
        turtle.right(91)
        spiral(n+2)
 
spiral(2)
wn.exitonclick()

