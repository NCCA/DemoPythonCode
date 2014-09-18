#!/usr/bin/python

class Parent(object):

	def foo(self):
		print "foo called self=%s" %(self)

	def bar(self) :
		print "bar called self=%s" %(self)

	def __str__(self) :
		return "Parent"

###########################################
class Child(Parent):
	def foo(self):
		print "foo called self=%s" %(self)

	def __str__(self) :
		return "Child"

###########################################

parent = Parent()
child = Child()

parent.foo()
child.foo()
parent.bar()
child.bar()
