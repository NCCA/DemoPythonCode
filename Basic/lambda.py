#!/usr/bin/python
import math
a=[1,2,3,4,5]
b=map(lambda x: x+1 , a)
print b

To=[0.0,0.0,0.0]
From=[0.0,4.0,3.0]


print To,From

direction = map(lambda x,y : x-y , To,From)
print direction
# get the length
len = math.sqrt(sum(map(lambda x : x*x , direction )))
print len
# divide by length
normal= map(lambda x : x/len , direction)
print normal
