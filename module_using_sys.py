import sys
import os
from math import sqrt
import math


print "1) Square root of 16 is", sqrt(16)
print "2) Square root of 16 is", math.sqrt(16)

print('the command line argument are:')
for i in sys.argv:
    print i

print '\n\n\n\n\nThe PYTHONPATH is ', sys.path, '\n'

print os.getcwd()

