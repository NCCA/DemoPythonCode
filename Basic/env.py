#!/usr/bin/python
import os

for env in os.environ :
	print "Variable = %s \nValue = %s"%(env, os.environ.get(env))