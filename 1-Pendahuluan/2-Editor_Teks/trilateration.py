#!/usr/bin/env python

import math
import numpy
from numpy import *
from math import *

#assuming elevation = 0
earthR = 6371
latA = -6.183212 #-6.181988#-6.181244
lonA = 106.8218 #106.822648#106.822084
DistA = 0.19 #0.256710701754
LatB = -6.181149 #-6.181931#-6.181056
LonB = 106.820984 #106.822647#106.821939
DistB = 0.19 #0.234592423446
LatC = -6.181058 #-6.181093
LonC = 106.820763 #106.822526#106.821535
DistC = 0.19 #0.0548954278262

#using authalic sphere
#if using an ellipsoid this step is slightly different
#convert geodetic Lat/Long to ECEF xyz
#   1. Convert Lat/Long to radians
#   2. Convert Lat/Long(radians) to ECEF
xA = earthR *(math.cos(math.radians(LatA)) * math.cos(math.radians(LonA)))
yA = earthR *(math.cos(math.radians(LatA)) * math.sin(math.radians(LonA)))