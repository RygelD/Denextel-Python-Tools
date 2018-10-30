# Run to find code for importing ScreenKit
__version__ = 0.1
RELEASE = 0.1
import sys
import os
print('import sys\nsys.path.insert(0,' + str(os.dirname(os.abspath(__file__))) + ')')
