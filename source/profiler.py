"""Use Robert Kern's line_profiler package.

Download: http://pypi.python.org/pypi/line_profiler
Documentation: http://packages.python.org/line_profiler/

Usage:
    kernprof.py -lv profiler.py
"""

@profile
def slow(x):
    result = []
    for item in x:
        result.insert(0, item)
    return result

if __name__ == '__main__':
    slow(range(100))
