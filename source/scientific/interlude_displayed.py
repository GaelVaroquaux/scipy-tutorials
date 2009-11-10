import scipy as sp
import numpy as np
import pylab as pl

l = sp.lena()
l = l[235:235+153, 205:162+205]

t = pl.imread('tarek.jpg')
t = t[::-1, ...]
t = t.sum(axis=-1)

pl.figure()
pl.imshow(t, cmap=pl.cm.gray)
pl.axis('off')

pl.figure()
pl.imshow(l, cmap=pl.cm.gray)
pl.axis('off')

t = t.astype(np.float)
t /= t.max()

l = l.astype(np.float)
l /= l.max()

pl.figure()
pl.imshow(t + l, cmap=pl.cm.gray)
pl.axis('off')


