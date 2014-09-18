#!/usr/bin/python

from ColourPrivate import *


red=ColourPrivate()
red.__r=1.0
print red.getR()
red.debugprint()
red.setR(1.0)
print red.getR()
