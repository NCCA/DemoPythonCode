#!/usr/bin/python

import os
import sys

def Usage() :
	print "ReadFile [filename]"

def main(argv=None):
# check to see if we have enough arguments
	if len(sys.argv) !=2 :
		Usage()
	else :
		# get the old and new file names
		FileName=sys.argv[1]
		if (os.path.exists(FileName)) :
			FILE=open(FileName,"r")
			lines=FILE.readlines()
			# now we have read the data close the file
			FILE.close()
			LineNum=0
			for line in lines :
				print "%04d %s" %(LineNum,line),
				LineNum+=1

if __name__ == "__main__":
    sys.exit(main())








