import numpy as np
import pylab as pl
x, y = np.mgrid[-5:5, -5:5]
u = -x
v = y
pl.quiver(x, y, u, v)
