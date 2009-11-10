
import time
import numpy as np

# Warm the cache
x = np.linspace(-100, 100, 1e7)
y = np.linspace(-100, 100, 1e7)
r = np.sqrt(x**2 + y**2)

print "Not in place"

for _ in range(3):
    x = np.linspace(-100, 100, 3e7)
    y = np.linspace(-100, 100, 3e7)
    start = time.time()
    r = np.sqrt(x**2 + y**2)
    print time.time() - start

print "In place"

for _ in range(3):
    x = np.linspace(-100, 100, 3e7)
    y = np.linspace(-100, 100, 3e7)
    start = time.time()
    x **= 2
    y **= 2
    x += y
    r = np.sqrt(x, x)
    print time.time() - start

