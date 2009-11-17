import numpy as np
import scipy as sp
import pylab as pl
from scipy import ndimage, signal
l = sp.lena()[200:-140, 190:-150]
l = l/float(l.max())
g = l + .13*np.random.normal(size=l.shape)

pl.figure(figsize=(12, 4.5))
pl.axes([0, 0, 0.3, 1])
pl.gray()
pl.imshow(ndimage.gaussian_filter(g, 1.6), vmin=0, vmax=1)
pl.title('Gaussian filter')
pl.axis('off')
pl.axes([0.35, 0, 0.3, 1])
pl.imshow(signal.medfilt2d(g, 5), vmin=0, vmax=1)
pl.title('Median filter')
pl.axis('off')
pl.axes([0.7, 0, 0.3, 1])
pl.imshow(signal.wiener(g, (5, 5)), vmin=0, vmax=1)
pl.title('Wiener filter')
pl.axis('off')
