#!/usr/bin/python

with open('/etc/passwd', 'r') as f:
	data=f.readlines()
	print data