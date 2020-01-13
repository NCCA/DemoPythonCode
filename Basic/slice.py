#!/usr/bin/python
from __future__ import print_function
a=range(0,10)
print('a[::2] ',a[::2])
print('a[::-1] ',a[::-1])
print('a[1:10:2]',a[1:10:2])
print('a[:-1:1] ',a[:-1:1])
del a[::2]
print('del a[::2] ',a)
print('range(10)[slice(0, 5, 2)]',range(10)[slice(0, 5, 2)])
