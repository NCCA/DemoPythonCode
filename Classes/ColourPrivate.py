#!/usr/bin/python

class ColourPrivate :
	' a very simple colour container'
	def __init__(self,r=0.0,g=0.0,b=0.0,a=1.0) :
		'constructor to set default values'
		self.__r=r
		self.__g=g
		self.__b=b
		self.__a=a

	def debugprint(self) :
		' method to print out the colour data for debug'
		print '[%f,%f,%f,%f]' %(self.__r,self.__g,self.__b,self.__a)

	def setR(self,r) :
		self.__r=r
	def getR(self) :
		return self.__r

	def setG(self,g) :
		self.__g=g
	def getG(self) :
		return self.__g

	def setB(self,b) :
		self.__b=b
	def getB(self) :
		return self.__b

	def setA(self,a) :
		self.__a=a
	def getA(self) :
		return self.__a

	def mix(self,colour,t) :
		'''method to mix current colour with another by t
		will catch the attribute error and pass back black if
		wrong values are passed
		'''
		c=Colour()
		try :
			c.__r=self.__r+(colour.__r-self.__r)*t
			c.__g=self.__g+(colour.__g-self.__g)*t
			c.__b=self.__b+(colour.__b-self.__b)*t
			c.__a=self.__a+(colour.__a-self.__a)*t
		except AttributeError, e:
			pass

		return c