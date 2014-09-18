#!/usr/bin/python

class DelTest :
	def __init__(self) :
		'constructor to set default values'
		print "init"

	def __del__(self) :
		print "deleted"