class Colour:
	# ctor to assign values
	def __init__(self, r=0, g=0, b=0,a=1):
		self.r=float(r)
		self.g=float(g)
		self.b=float(b)
		self.a=float(a)

	# debug print function to print vector values
	def __str__(self):
		return '[%f,%f,%f,%f]' %(self.r,self.g,self.b,self.a)