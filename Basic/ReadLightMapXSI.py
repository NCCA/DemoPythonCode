########################################################################
# This function is to read a LightMap File from the MedianCutFilter
# Usage ReadLighMap(Name of file, Name of Light Group)
# Author Jon Macey jmacey@bmth.ac.uk
# Version 1.0 15/1/08
# This is to be used with XSI 6.5 and above
########################################################################


import win32com
import time
from array import array
import random
import sys
import math
from math import *
xsi = Application
oRoot = Application.ActiveSceneRoot





	
# main function
def ReadLightMap(GroupName):
	# first create a group to add the lights to
	xsi.CreateGroup(GroupName, "", "")
	oFileBrowser = XSIUIToolkit.FileBrowser
	oFileBrowser.DialogTitle="Please Select LightMap file"
	oFileBrowser.Filter = "LightMap (*.lightmap)|*.lightmap||" 
	oFileBrowser.ShowOpen()
	
	if oFileBrowser.FilePathName == "" :
		print "No file selected"
		return
	fileName=oFileBrowser.FilePathName
	
	
	# LightNum used to append to GroupName for the Light
	LightNum=0
	# so we open the file for reading
	lightFile=open(fileName,'r')
	# read in all the data
	try :
		data=lightFile.readlines()
		#now read through the file and grab data
		for line in data :
			# tokenise the data into tuple light
			light=line.split()
			# File Line Format is x,y,z r,g,b, Shadowed[1,0], Intensity
			# we need to use the constructors for float to ensure we get floats not strings
			x=float(light[0])
			y=float(light[1])
			z=float(light[2])
			r=float(light[3])
			g=float(light[4])
			b=float(light[5])
			# we convert shad to an int
			shad=int(light[6])
			intensity=float(light[7])
			# create a name for the light
			LightName=GroupName+"%d" %(LightNum)
			# now run xsi commands to create the light dome from map

			Light=oRoot.AddLight("Point",False,LightName);
			xsi.SelectObj(LightName, "", 1)
			xsi.Translate("", x, y, z, "siAbsolute", "siGlobal", "siObj", "siXYZ", "", "", "", "", "", "", "", "", "", 0, "")
			Intensity=LightName+".light.soft_light.intensity"
			xsi.SetValue(Intensity, intensity, "")
			Shadow=LightName+".light.soft_light.shadow"
			xsi.SetValue(Shadow, 1, "")
			xsi.AddToGroup(GroupName, LightName)
			colour=LightName+".light.soft_light.color.red"
			xsi.SetValue(colour, r, "")
			colour=LightName+".light.soft_light.color.green"
			xsi.SetValue(colour, g, "")
			colour=LightName+".light.soft_light.color.blue"
			xsi.SetValue(colour, b, "")

			xsi.AddToGroup(GroupName, LightName)

			LightNum+=1;
	finally :
		# finished with the file so close
		lightFile.close()

ReadLightMap("NameOfGroup")