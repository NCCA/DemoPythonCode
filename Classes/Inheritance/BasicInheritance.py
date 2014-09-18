#!/usr/bin/python

class Parent(object):

	def foo(self):
		print "foo called self=%s" %(self)

	def __str__(self) :
		return "Parent"

class Child(Parent):
    pass

parent = Parent()
child = Child()

parent.foo()
child.foo()