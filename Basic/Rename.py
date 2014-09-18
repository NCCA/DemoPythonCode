#!/usr/bin/python

import os
import shutil
import sys

def Usage() :
	print "Rename OldName NewName"

def main(argv=None):
# check to see if we have enough arguments
	if len(sys.argv) !=3 :
		Usage()
	else :
		# get the old and new file names
		OldName=sys.argv[1]
		NewName=sys.argv[2]
		# get the files in the current directory
		Files=os.listdir(".")
		# for each file
		for file in Files :
			# see if it starts with the old name
			if file.startswith(OldName) :
				# make a copy of the old file name
				oldfile=file;
				# now we break down the string so we can
				# build the new file name
				file=file.split(".")
				file[0]=NewName
				file="%s.%s.%s" %(file[0],file[1],file[2])
				# finally we rename the file (using move)
				shutil.move(oldfile,file)


if __name__ == "__main__":
    sys.exit(main())