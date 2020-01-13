#!/usr/bin/python
from __future__ import print_function
n =((a,b)for a in range(0,5)for b in range(0,5))
for i in n :
	print(i)