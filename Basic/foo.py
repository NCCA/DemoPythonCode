#!/usr/bin/python
import sys

def foo(argv=None):
	print "in foo function"
	print "my name is ",__name__



if __name__ == "__main__":
    sys.exit(foo())