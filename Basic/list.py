#!/usr/bin/python
from __future__ import print_function
data = [123,"hello",2.45,3+2J]
moreData=[" ","world"]

print(data)
print(data[1])
print(data[2:])

hello=data[1]+moreData[0]+moreData[1]
print(hello)

for i in range(0,len(data)) :
	print(data[i])
print('Using enumerate which gives us a number and value')
for num,ch in enumerate(data) :
	print('{} {}'.format(num,ch))