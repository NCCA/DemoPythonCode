#!/usr/bin/python
from __future__ import print_function
a=range(0,5)
a*=2
print(a)
b=set(a)
print(b)


a =set([1,2,3,4])
b =set([3,4,5,6])
print ("a=",a)
print ("b=",b)
print ("union a | b",a | b)
print ("intersection a & b" ,a & b)
print ("subset false a<b",a < b)
print ("difference a-b",a - b)
print ("Symmetric diff a^b",a ^ b)
