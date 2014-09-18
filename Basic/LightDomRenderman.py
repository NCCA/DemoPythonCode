#!/usr/bin/python
# for bash we need to add the following to our .bashrc
# export PYTHONPATH=$PYTHONPATH:$RMANTREE/bin   
import getpass
import time,random,math
# import the python renderman library
import prman


	
def Scene(ri) :
	
	

	ri.TransformBegin()
	ri.Translate( 0, -0.9, 0)
	ri.Scale( 1 ,0.4, 1)
	ri.Color([1,1,1])
	ri.Surface("paintedplastic")
	ri.Patch( "bilinear",{ "P" : [-0.5, -0.5, 0.5,-0.5, 0.5 ,0.5 ,0.5, -0.5, 0.5 ,0.5, 0.5, 0.5] })      
	ri.Patch( "bilinear",{ "P" :  [-0.5 ,-0.5 ,-0.5 ,-0.5 ,0.5, -0.5, 0.5 ,-0.5, -0.5, 0.5 ,0.5 ,-0.5] })  
	ri.Patch( "bilinear",{ "P" :  [-0.5 ,-0.5 ,-0.5 ,-0.5, 0.5 ,-0.5 ,-0.5 ,-0.5 ,0.5 ,-0.5, 0.5 ,0.5] })  
	ri.Patch( "bilinear",{ "P" :  [0.5 ,-0.5 ,-0.5 ,0.5 ,0.5 ,-0.5 ,0.5 ,-0.5 ,0.5 ,0.5 ,0.5, 0.5] })     
	ri.Patch( "bilinear",{ "P" :  [0.5, -0.5, 0.5 ,0.5 ,-0.5, -0.5, -0.5 ,-0.5 ,0.5, -0.5 ,-0.5, -0.5] })  
	ri.Patch( "bilinear",{ "P" :  [0.5, 0.5, 0.5 ,0.5 ,0.5, -0.5, -0.5 ,0.5 ,0.5 ,-0.5 ,0.5 ,-0.5] })
	ri.TransformEnd()
	
	ri.TransformBegin()
	ri.Translate( 0.5, -1.0, -1.5)
	ri.Scale (0.2 ,0.2 ,0.2)
	ri.Rotate (-90, 1 ,0 ,0)
	ri.Rotate (55, 0, 0, 1)
	ri.Color([1,1,1])
	ri.Surface("paintedplastic")

	ri.Geometry ("teapot")
	ri.TransformEnd()
	
	ri.TransformBegin()
	ri.Translate( 0, -0.7, 0)
	ri.Scale( 0.2, 0.2, 0.2)
	ri.Rotate( -90, 1 ,0 ,0)
	ri.Rotate( 55, 0, 0, 1)
	ri.Color([1,1,1])
	ri.Surface("paintedplastic")

	ri.Geometry( "teapot")
	ri.TransformEnd()
	ri.TransformBegin()
	ri.Color([1,1,1])
	ri.Surface("paintedplastic")
	
	ri.Translate( 1.3, -0.5 ,.2)
	ri.Rotate( 90, 1, 0, 0)
	ri.Scale( 0.2, 0.2, 1.4)
	ri.Cylinder( 1, -0.5, 0.5, 360) 
	ri.TransformEnd()
	ri.TransformBegin()
	ri.Translate( 1.3, 0.2, .2)
	ri.Rotate( 90, 1 ,0 ,0)
	ri.Scale( 0.2, 0.2, 2)
	ri.Disk( 0, 1 ,360)
	ri.TransformEnd()
	
	ri.TransformBegin()
	ri.Translate( -1.3, -1, .2)
	ri.Rotate( 130, 0 ,1 ,0)
	ri.Scale( 0.01, 0.01, 0.01)
	ri.Surface("paintedplastic",{"string texturename":["troll.tx"]})
	ri.ReadArchive("CaveTroll2.rib")
	ri.TransformEnd()
	
	face=[-0.1,-1,-3, 0.1,-1,-3,-0.1,-1,3, 0.1,-1,3]
	plank=-5.0
	
	ri.AttributeBegin()
	while (plank <=5.0) :
		ri.TransformBegin()
		ri.Color([1,1,1])
		ri.Surface("paintedplastic")
		ri.Translate(plank,0,0)
		ri.Patch("bilinear",{'P':face})
		ri.TransformEnd()
		plank=plank+0.206
	ri.AttributeEnd()

	
prman.Init(["-progress"])  # a list of string arguments, same as prman executable	
ri = prman.Ri() # create an instance of the RenderMan interface
ri.Option("rib", {"string asciistyle": "indented"})



filename = "paintedplastic.rib"
# this is the begining of the rib archive generation we can only
# make RI calls after this function else we get a core dump
ri.Begin("__render") #filename)
ri.Clipping(0.1,20)

# ArchiveRecord is used to add elements to the rib stream in this case comments
# note the function is overloaded so we can concatinate output
ri.ArchiveRecord(ri.COMMENT, 'File ' +filename)
ri.ArchiveRecord(ri.COMMENT, "Created by " + getpass.getuser())
ri.ArchiveRecord(ri.COMMENT, "Creation Date: " +time.ctime(time.time()))


# now we add the display element using the usual elements
# FILENAME DISPLAY Type Output format

ri.Display( "AllPasses.exr", "framebuffer","rgb")
# Specify PAL resolution 1:1 pixel Aspect ratio
ri.Format(1024,720,1)
ri.ShadingRate(1)
ri.PixelSamples(2,2)
ri.Clipping(1,10)

ri.Attribute("visibility", {"int diffuse" :1,
							"int specular": 1,
							"int transmission": 1})
							
							
ri.Attribute("trace",  {"int maxdiffusedepth" :[1], "int maxspeculardepth" : [2],
  						"int displacements" : [0] , "bias" : [.01],
  						"int samplemotion" : [0]})
 
							
							

# now set the projection to perspective
ri.Projection(ri.PERSPECTIVE,{ri.FOV:50}) 
ri.ReadArchive("pisa.rib")

ri.Translate( 0 ,0.0, 3)
ri.Rotate (-10 ,1, 0 ,0)
ri.Rotate( 35 ,0 ,1 ,0)
"""
#normal view
ri.Translate(0,0,4)
"""
# now we start our world
ri.WorldBegin()


Scene(ri)

ri.WorldEnd()

# and finally end the rib file
ri.End()
