#!/usr/bin/python
from os import *
from os.path import *
import shutil

import os, commands, getopt, sys

def usage() :
	print "**************************************************************************"
	print "repad.py re-number file sequences"
	print "Version 1.0 by jmacey@bmth.ac.uk"
	print "**************************************************************************"
	print "At present it only works for files of the format Name.###.ext\n"
	print "The script will process all files it finds in the current directory "
	print "If only certain files are to be processed use the -f Filter Option"
	print "\nOptions :\n"
	print "-p --pad set the pad level e.g. -p 9 will give the output Example.000000001.tiff"
	print "-f --filter [\"filter\"] only process files containing the text \"filter\""
	print "-r --rename [\"new name\"] rename the file as well\n"
	print "\nThis works on the whole file name so for example :\n"
	print "repad.py -p 5 -f tiff would search for all tiff files"
	print "repad.py -p 6 -f AOPass would search for files containing the text AOPass\""
	print "\n-h --help print this help\n"

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg
        print "Unknown Option"
        usage()

def main(argv=None):
	if argv is None:
		argv = sys.argv
	# process the command line options
	try:
		try:
			opts, args = getopt.getopt(argv[1:], "hp:f:r:", ["help","pad=","filter=","rename="])
		except getopt.error, msg:
			raise Usage(msg)
    	except Usage, err:
			print >>sys.stderr, err.msg
			print >>sys.stderr, "for help use --help"
			return 2
	# default file pad is 4 i.e. .0001.
	PAD=4
	# by default try and process all files in the directory
	FILTER=False
	# by default dont rename the file as well
	RENAME=False
	RenameString=[]
	# the string to contain the filter text
	FiltString=[]
	for opt, arg in opts:
		# set the padding value converting from the command line string to an int
		if opt in ("-p", "--pad"):
			PAD=int(arg)
		elif opt in ("-h","--help") :
			usage()
			return
		# find the filter string
		elif opt in ("-f","--filter") :
			FILTER=True
			FiltString=arg
		elif opt in ("-r","--rename") :
			RENAME=True
			RenameString=arg


	# ok this is cool (try doing it in C++) we create a string containing our format specifier
	# i.e. %09d (using PAD as the variable to specify the numeric value)
	# this is then used later to pass the value we want for the number of the file
	# this works as Python evaluates as it goes (interprets) the string, also note to use a % in the
	# string we need to use %% (a la C)

	str="%%0%dd" %(PAD)
	# get all the files in the current directory
	FileNames=listdir(".")
	# now loop through all the files
	ConvCount=0
	for Files in FileNames :
		# split the file name into sections
		name=Files.split(".")
		# if filter option has been set see if it is in the string
		if(FILTER== True) :
			if(Files.rfind(FiltString) == -1) :
				continue

		# if we have 3 elements to the filename (not the best check as it could be wrong)
		if len(name) ==3 :
			if(RENAME == True) :
				name[0]=RenameString
			#build the new file name with the padding
			outputname=name[0]+"."+str %(int(name[1]))+"."+name[2]
			# this should be portable over different os's but it basically calls the move / mv command
			# to copy the file to the new name
			shutil.move(Files,outputname)
			ConvCount+=1
	print "Files Converted ",ConvCount


if __name__ == "__main__":
    sys.exit(main())

