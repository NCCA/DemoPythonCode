#!/usr/bin/python

#!/usr/bin/python

import sys
import argparse
import inspect

def main(shadingrate=10,pixelvar=0.1,
         fov=48.0,width=1024,height=720,
         integrator='PxrPathTracer',integratorParams={}
        ) :
	args, _, _, _ = inspect.getargvalues(inspect.currentframe()) 
	for arg in args: 
		print arg , locals()[arg]


if __name__ == '__main__':
	parser=argparse.ArgumentParser()
	parser = argparse.ArgumentParser(description='Modify render parameters')

	parser.add_argument('--shadingrate', '-s', nargs='?', 
											const=10.0, default=10.0, type=float,
											help='modify the shading rate default to 10')

	parser.add_argument('--pixelvar', '-p' ,nargs='?', 
											const=0.1, default=0.1,type=float,
											help='modify the pixel variance default  0.1')
	parser.add_argument('--fov', '-f' ,nargs='?', 
											const=48.0, default=48.0,type=float,
											help='projection fov default 48.0')
	parser.add_argument('--width' , '-wd' ,nargs='?', 
											const=1024, default=1024,type=int,
											help='width of image default 1024')
	parser.add_argument('--height', '-ht' ,nargs='?', 
											const=720, default=720,type=int,
											help='height of image default 720')

	parser.add_argument('--rib', '-r' , action='count',help='render to rib not framebuffer')
	parser.add_argument('--default', '-d' , action='count',help='use PxrDefault')
	parser.add_argument('--vcm', '-v' , action='count',help='use PxrVCM')
	parser.add_argument('--direct', '-t' , action='count',help='use PxrDirect')
	parser.add_argument('--wire', '-w' , action='count',help='use PxrVisualizer with wireframe shaded')
	parser.add_argument('--normals', '-n' , action='count',help='use PxrVisualizer with wireframe and Normals')
	parser.add_argument('--st', '-u' , action='count',help='use PxrVisualizer with wireframe and ST')

	args = parser.parse_args()
	if args.rib :
		filename = 'rgb.rib' 
	else :
		filename='__render'

	integratorParams={}
	integrator='PxrPathTracer'
	if args.default :
		integrator='PxrDefault'
	if args.vcm :
		integrator='PxrVCM'
	if args.direct :
		integrator='PxrDirectLighting'
	if args.wire :
		integrator='PxrVisualizer'
		integratorParams={'int wireframe' : [1], 'string style' : ['shaded']}
	if args.normals :
		integrator='PxrVisualizer'
		integratorParams={'int wireframe' : [1], 'string style' : ['normals']}
	if args.st :
		integrator='PxrVisualizer'
		integratorParams={'int wireframe' : [1], 'string style' : ['st']}


	main(args.shadingrate,args.pixelvar,args.fov,args.width,args.height,integrator,integratorParams)






