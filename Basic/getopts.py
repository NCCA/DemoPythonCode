#!/usr/bin/python


import  getopt, sys

def usage() :
	print "to use the program pass -l for long mode"
	print "-f [name] for file mode"

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg
        print "Unknown Option\n\n"
        usage()

def main(argv=None):
	if argv is None:
		argv = sys.argv
	# process the command line options
	try:
		try:
			opts, args = getopt.getopt(argv[1:], "hlf:s", ["help","long","file=","short"])
		except getopt.error, msg:
			raise Usage(msg)
    	except Usage, err:
			print >>sys.stderr, err.msg
			print >>sys.stderr, "for help use --help"
			return 2

	for opt, arg in opts:
		if opt in ("-l", "--long"):
			print "long mode"
		elif opt in ("-h","--help") :
			usage()
			return
		elif opt in ("-f","--file") :
			print "File Mode name passed ",arg
		elif opt in ("-s","--short") :
			print "short"
	print "Now in Main Program"

if __name__ == "__main__":
    sys.exit(main())














