# Run to find code for importing ScreenKit
import sys
import os
print('import sys\nsys.path.insert(0,' + str(os.path.abspath(os.path.join(sys.path, os.pardir))) + ')')
