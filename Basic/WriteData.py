#!/usr/bin/python

import os
import shutil
import sys
# import the uniform function from random
from random import uniform

def Usage() :
	print "WriteData [filename] Number"

def main(argv=None):
# check to see if we have enough arguments
	if len(sys.argv) !=3 :
		Usage()
	else :
		# get the file name to write to
		FileName=sys.argv[1]
		# convert the 2nd argument to an int
		Num=int(sys.argv[2])
		# try to open the file
		try :
			FILE=open(FileName,"w")
		# if this fails catch the error and exit
		except IOError :
			print "Error opening file",FileName
			return
		# loop and create some ranom values to write to the file
		for i in range(0,Num) :
			FILE.write("Point %f %f %f\n" %(uniform(-10,10),uniform(-10,10),uniform(-10,10)) )
		# finally close the file
		FILE.close()
if __name__ == "__main__":
    sys.exit(main())








