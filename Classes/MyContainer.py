
class MyContainer :
	''' a very simple container class '''
	def __init__(self,data=None) :
		if data is None :
			self.data=[]
		else :
			self.data=data

	def __str__(self) :
		''' method to print out the container contents'''
		return ','.join(map(str, self.data))

	def __len__(self) :
		''' return the length of the data'''
		return len(self.data)

	def __getitem__(self,index) :
		''' access an item in the container a=c[n]'''
		return self.data[index]

	def __setitem__(self,index,value) :
		''' set an item in the container c[n]=v'''
		self.data[index]=value

	def __delitem__(self,index) :
		''' remove an item at n del c[1]'''
		del self.data[index]

	def __iter__(self):
		''' return an iterator to the data item'''
		return iter(self.data)

	def __reversed__(self):
		''' return the reversed version of the data for the reversed function'''
		return MyContainer(reversed(self.data))

	def append(self,value) :
		''' our own append method to add to the data'''
		self.data.append(value)














