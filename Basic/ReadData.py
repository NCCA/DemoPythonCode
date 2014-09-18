#!/usr/bin/python

import os
import shutil
import sys
# import the uniform function from random
from random import uniform

def Usage() :
	print "ReadData [filename] "

def main(argv=None):
# check to see if we have enough arguments
	if len(sys.argv) !=2 :
		Usage()
	else :
		# get the file name to write to
		FileName=sys.argv[1]
		# try to open the file
		try :
			FILE=open(FileName,"r")
		# if this fails catch the error and exit
		except IOError :
			print "Error opening file",FileName
			return
		# loop and create some ranom values to write to the file
		Lines=FILE.readlines()
		FILE.close()
		for line in Lines :
			# lets see if the line is a point
			if line.startswith("Point") :
				# now split it and convert it to a numberic value
				line=line.split()
				try :
					x=float(line[1])
					y=float(line[2])
					z=float(line[3])
					print "%f %f %f" %(x,y,z)
				except ValueError :
					print line
if __name__ == "__main__":
    sys.exit(main())












