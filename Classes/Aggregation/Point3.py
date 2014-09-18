class Point3:
	# ctor to assign values
	def __init__(self, x=0.0, y=0.0, z=0.0):
		self.x=float(x)
		self.y=float(y)
		self.z=float(z)
	# debug print function to print vector values
	def __str__(self):
		return  '[%f,%f,%d]' %(self.x,self.y,self.z)