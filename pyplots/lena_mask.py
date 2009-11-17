import numpy as np
import scipy as sp
import pylab as pl
pl.figure(1)
pl.clf()
l = sp.lena()
n, m = l.shape
x, y = np.indices((n, m))
d = np.sqrt((x - 0.5*n)**2 + (y - 0.5*m)**2)
l[d > 200] = 255
pl.imshow(l, cmap=pl.cm.gray)
pl.axis('off')
