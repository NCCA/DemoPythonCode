#!/usr/bin/python
from __future__ import print_function
import numpy as np


xy= [(ix, iy) for ix in np.arange(-1.0,1.0,0.5)
              for iy in np.arange(-1.0,1.0,0.5)]
for i,num in enumerate(xy) :
  print(i,num)