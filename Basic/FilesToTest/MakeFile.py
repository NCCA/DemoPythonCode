#!/usr/bin/python

import os
Name="Test.%03d.png"

for i in range(0,20) :
	file=Name %(i)
	os.system("touch %s" %(file))
