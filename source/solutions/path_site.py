"""Script to search the PYTHONPATH for the module site.py"""

import os
import sys
import glob

def find_module(module):
    result = []
    for subdir in sys.path:
        pth = os.path.join(subdir, module)
        res = glob.glob(pth)
        if len(res) > 0:
            result.append(res)
    return result


if __name__ == '__main__':
    result = find_module('site.py')
    print result
    
