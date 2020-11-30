# Imports standard python functionality
import sys
import os

base_dir = os.path.dirname(__file__) or '.'

# Import lib trade functionality
trade_dir = os.path.join(base_dir, '..\..\..\lib\\trade')
sys.path.insert(1, trade_dir)
from tra_pivot_point import *
from tra_support import *

print (len(sys.argv))
print (str(sys.argv))

pivotPoint = PivotPoint()
support = Support()
pivotPoint.calculatePivotPoint(10.0, 9.0,9.5)
pp = pivotPoint.getValue()
support.calculateSupportLevels(pp, 10.0, 9.0, 9.5)
# Usage: python .\print_support_levels.py [int]
supp = support.getSupportLevel(ESupportLevels(int(sys.argv[1],10)))
print (supp)