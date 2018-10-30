# Run to find code for importing ScreenKit
import sys
import os
print('import sys\nsys.path.insert(0,' + str(os.dirname(os.abspath(__file__))) + ')')
