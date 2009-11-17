import numpy as np
import scipy as sp
import pylab as pl
from scipy import ndimage
l = sp.lena()
pl.figure(figsize=(12, 4.5))
pl.gray()
pl.axes([0, 0, 0.30, 1])
pl.imshow(l)
pl.axis('off')
pl.axes([0.35, 0, 0.3, 1])
pl.imshow(ndimage.gaussian_filter(l, 5))
pl.axis('off')
pl.axes([0.7, 0, 0.3, 1])
pl.imshow(ndimage.gaussian_gradient_magnitude(l, 3))
pl.axis('off')
