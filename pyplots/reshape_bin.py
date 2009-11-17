
import numpy as np
import pylab as pl

x, y = np.ogrid[0:10, 0:10]
r = np.sqrt(x**2 + y**2)
pl.matshow(r)

r_binned = r.reshape((5, 2, 5, 2)).sum(axis=-1).sum(axis=1)
pl.matshow(r_binned)


