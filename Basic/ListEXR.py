#!/usr/bin/python

import os

Files=os.listdir(".")

for file in Files :
	if file.endswith(".exr") :
		print file
