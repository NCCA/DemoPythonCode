########################################################################
# This function is to read a LightMap File from the MedianCutFilter
# Usage ReadLighMap(Name of file, Name of Light Group)
# Author Jon Macey jmacey@bmth.ac.uk
# Version 1.0 15/1/08
# This is to be used with Houdini 9.0 and above
########################################################################

import hou


# main function
def ReadLightMap(fileName, GroupName,fov):
# first we get to obj level and create some vars etc
# first we get the object level

	net = hou.node("/obj")
	# create a networkbox for the lights
	nb=net.createNetworkBox(GroupName)
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
			# now run houdini commands to create the light dome from map

			# create a point light and reference it as clight
			# the default light is pointlight so no need to set it
			# may change this as could be changed!
			clight=net.createNode('hlight',LightName)

			#set the light position
			clight.parm('tx').set(x)
			clight.parm('ty').set(y)
			clight.parm('tz').set(z)


			# set the light colours
			clight.parm('light_colorr').set(r)
			clight.parm('light_colorg').set(g)
			clight.parm('light_colorb').set(b)
			# set intensity
			clight.parm('light_intensity').set(intensity)
			# set shadow on 0 = none 1= ray trace 3(not implemented but depth map)
			clight.parm('shadow_type').set(shad)
			# set the light fov based on the param passed in
			clight.parm('light_fov').set(fov)
			# parent it to the net box
			nb.addNode(clight)
			LightNum+=1;
	finally :
		# finished with the file so close
		lightFile.close()

ReadLightMap("/Volumes/home/jmacey/teaching/Python/CDE/Code2013/Basic/pisa.lightmap","LightDome",15)