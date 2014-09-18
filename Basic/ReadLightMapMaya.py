########################################################################
# This function is to read a LightMap File from the MedianCutFilter
# Usage ReadLighMap(Name of file, Name of Light Group)
# Author Jon Macey jmacey@bmth.ac.uk
# Version 1.0 15/1/08
# This is to be used with maya 8.0 and above
########################################################################

# import the maya commands to local namespace mc
import maya.cmds as mc
# main function
def ReadLightMap(fileName, GroupName):
	
	# create a group for the lights
	mc.group( em=True, name=GroupName);	
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
			# we convert shad to a boolean
			shad=bool(light[6])
			intensity=float(light[7])
			# create a name for the light
			LightName=GroupName+"%d" %(LightNum)
			
			# now run maya commands to create the light dome from map
			# create a point light
			#print LightName,x,y,z,r,g,b
			mc.pointLight(name=LightName,position=[x,y,z], rgb=[r,g,b] ,i=intensity ,rs=shad)
			# select it
			mc.select(LightName,r=True)
			# parent it to the group
			mc.parent(LightName,GroupName ,relative=True)
			LightNum+=1;
	finally :
		# finished with the file so close
		lightFile.close()
		
# to run the script use 
#ReadLightMap("ightmap file ","group name")
ReadLightMap("/Users/jmacey/teaching/LightTools/images/pisa.lightmap","LightDome")
	
	
	
	
	
	