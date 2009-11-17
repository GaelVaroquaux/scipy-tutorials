import numpy as np
import scipy as sp
import pylab as pl
l = sp.lena()
pl.figure(figsize=(9, 4.5))
pl.gray()
pl.axes([0, 0, 0.45, 1])
pl.imshow(l)
pl.axis('off')
pl.axes([0.55, 0, 0.45, 1])
pl.imshow(l[:-2, 1:-1] - l[2:, 1:-1] + l[1:-1, :-2] - l[1:-1, 2:])
pl.axis('off')
