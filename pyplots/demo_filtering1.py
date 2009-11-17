import numpy as np
import scipy as sp
import pylab as pl
from scipy import ndimage, signal
l = sp.lena()[200:-140, 190:-150]
l = l/float(l.max())
pl.figure(figsize=(12, 4.5))
pl.axes([0.15, 0, 0.3, 1])
pl.gray()
pl.imshow(l, vmin=0, vmax=1)
pl.title('Ground truth')
pl.axis('off')
pl.axes([0.5, 0, 0.3, 1])
g = l + .13*np.random.normal(size=l.shape)
pl.imshow(g, vmin=0, vmax=1)
pl.title('Noisy observation')
pl.axis('off')

