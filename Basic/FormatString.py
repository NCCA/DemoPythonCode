#!/usr/bin/python

# declare a string

Name="BeautyPass.%04d.exr"

for i in range(0,4) :
	print Name %(i)

Name="Pass"
frame=2
Ext="tiff"

FullName ="%s.%04d.%s" %(Name,frame,Ext)
print FullName