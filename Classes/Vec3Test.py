#!/usr/bin/python

from Vec3 import *

v1=Vec3(1,2.0,1.0)
print "testing v1==v1" ,v1==v1
print v1
v2=Vec3(0.4,2.0,1.0)

print "testing v1==v2 ",v1==v2
print "testing v1!=v2 ",v1!=v2
print "testing v1!=v1 ",v1!=v1
print "testing v1+v2 ",v1+v2
print "testing v1-v2 ",v1-v2
print "testing v1*2 ",v1*2
print "testing 2*v1 ",2*v1
v1*=0.5
print "testing v1 *=0.5 ",v1
v1+=v2
print "testing v1+=v2 ",v1
