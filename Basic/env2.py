#!/usr/bin/python
import os

if ( os.environ.get("PROJECTDIR") == "/tmp") :
	print "project ok"
else :
	print "project not ok"