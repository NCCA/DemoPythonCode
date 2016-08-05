#!/usr/bin/python


def foo(data) :
	print "foo ",data

def bar(_data) :
	print "bar ",_data


functions=[foo,bar]

functions[0](12)
functions[1](12)
functions[0](99)
functions[1](88)






