#!/usr/bin/python
import sys

def main(argv=None):
	if argv is None:
		argv = sys.argv
	print argv
	for args in argv :
		print args


if __name__ == "__main__":
    sys.exit(main())