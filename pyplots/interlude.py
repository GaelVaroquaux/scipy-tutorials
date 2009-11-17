import scipy as sp
import numpy as np
import pylab as pl

l = sp.lena()
l_ = l[235:235+153, 205:162+205]

t = pl.imread('tarek.jpg')
t = t[::-1, ...]
t_ = t.sum(axis=-1)

################################################################################
pl.figure(0, figsize=(12, 4.5))
pl.gray()
pl.clf()
pl.axes([0, 0, 0.3, 1])
pl.imshow(t_.copy())
pl.axis('off')
pl.axes([0.33, 0, 0.3, 1])
pl.imshow(l_.copy())
pl.axis('off')

t_ = t_.astype(np.float)
t_ /= t_.max()

l_ = l_.astype(np.float)
l_ /= l_.max()

pl.axes([0.66, 0, 0.3, 1])
pl.imshow(t_ + l_)
pl.axis('off')


