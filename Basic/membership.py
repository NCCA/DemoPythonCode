#!/usr/bin/python
from __future__ import print_function 

data = (123,"hello",2.45,3+2J)
numbers=[1,2,3,4,5]
print( "world" in data)
print( "text" not in numbers)
print( 99 in numbers )
print( 2 in numbers )


imageTypes=['png','tiff','tif','jpg','gif']
# note use of lower to ensure we check against correct values
if 'TIFF'.lower() or 'jpg'.lower() in imageTypes :
  print('Have image')
