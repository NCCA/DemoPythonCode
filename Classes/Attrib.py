#!/usr/bin/python

class Attr :

	def __init__(self,x=1.0,y=1.0) :
		self.x=x
		self.y=y

	def __str__(self) :
		''' this method will return our data when doing something like print v '''
		return "[%r,%r]" %(self.x,self.y)

	def __getattr__(self,name) :
		print "the attrib %r doesn't exist" %(name)
		

	def __setattr__(self,name,value) :
		print "trying to set attribute %r=%r" %(name,value)
		self.__dict__[name] = value

	def __delattr__(self,name) :
		print "trying to delete %r " %(name)


a=Attr(1,1)
print a
print a.w
a.w=99
print a.w

del a.w
