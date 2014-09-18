#!/usr/bin/python
import sys
import foo

def main(argv=None):
	print "in main function"
	print __name__
	foo.foo()


if __name__ == "__main__":
    sys.exit(main())