#!/usr/bin/python

class Parent(object):

	def __init__(self,a) :
		self.a=a

	def foo(self):
		print "foo called self=%s a=%r" %(self,self.a)

	def __str__(self) :
		return "Parent"

###########################################
class Child(Parent):

	def __init__(self,a,b) :
		super(Child,self).__init__(a)
		self.b=b

	def foo(self):
		print "foo called self=%s a=%r b=%r" %(self,self.a,self.b)

	def __str__(self) :
		return "Child"

###########################################

parent = Parent(2)
child = Child('test' ,'values')

parent.foo()
child.foo()