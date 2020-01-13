from Point3 import Point3
from Colour import Colour



class Sphere :
	# ctor to assign values
	def __init__(self, pos=Point3(), colour=Colour(), radius=1,name=""):
		self.pos=pos
		self.colour=colour
		self.radius=radius
		self.name=name

	def Print(self):
		print "Sphere %s" %(self.name)
		print "Radius %d" %(self.radius)
		print "Colour",
		print self.colour
		print "Position ",
		print self.pos



class Ellipse :	

	def Print(self) :
		print "elipse"





