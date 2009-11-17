========================================
Scipy: numerical and scientific toolbox
========================================

.. 
   >>> import numpy as np
   >>> import scipy as sp
   >>> import pylab as pl


`scipy` is mainly composed of task-specific sub-modules:

============= ===============================================
cluster         Vector quantization / Kmeans
fftpack         Fourier transform
integrate       Integration routines
interpolate     Interpolation
io              Data input and output
linalg          Linear algebra routines
maxentropy      Routines for fitting maximum entropy models
ndimage         n-dimensional image package
odr             Orthogonal distance regression
optimize        Optimization
signal          Signal processing
sparse          Sparse matrices
spatial         Spatial data structures and algorithms
special         Any special mathematical functions
stats           Statistics
============= ===============================================

IO
===

* Load and save matlab files::

    >>> from scipy import io
    >>> struct = io.loadmat('file.mat', struct_as_record=True)
    >>> io.savemat('file.mat', struct)

See also:

    * Load text files::

        np.loadtxt/np.savetxt

    * Clever loading of text/csv files::

        np.genfromtxt/np.recfromcsv

    * Fast an efficient binary format::

        np.save/np.load


Optimization
=============

* Finding zeros of a function:

    >>> def f(x):
    ...     return x**3 - x**2 - 10
    >>> from scipy import optimize
    >>> optimize.fsolve(f, 1)
    2.5445115283877615

* Curve fitting:

.. plot:: pyplots/demo_curve_fit.py
    :include-source:


Statistics and random numbers
===================================

    >>> a = np.random.normal(size=1000)
    >>> bins = np.arange(-4, 5)
    >>> bins
    array([-4, -3, -2, -1,  0,  1,  2,  3,  4])
    >>> histogram = np.histogram(a, bins=bins)
    >>> bins = 0.5*(bins[1:] + bins[:-1])
    >>> bins
    array([-3.5, -2.5, -1.5, -0.5,  0.5,  1.5,  2.5,  3.5])
    >>> from scipy import stats
    >>> b = stats.norm.pdf(bins)

.. sourcecode:: ipython

    In [1]: pl.plot(bins, histogram)
    In [2]: pl.plot(bins, b)

.. plot:: pyplots/normal_distribution.py


Image processing
======================

::

    from scipy import ndimage
    l = sp.lena()
    pl.imshow(ndimage.gaussian_filter(l, 5), cmap=pl.cm.gray)
    pl.imshow(ndimage.gaussian_gradient_magnitude(l, 3), cmap=pl.cm.gray)

.. plot:: pyplots/lena_ndimage.py

Interpolation
==============

::

    x = np.arange(10)
    y = np.sin(x)

    pl.plot(x, y, '+', markersize=10)

    from scipy import interpolate

    f = interpolate.interp1d(x, y)
    X = np.linspace(0, 9, 100)
    pl.plot(X, f(X), '--')

    f = interpolate.interp1d(x, y, kind='cubic')
    X = np.linspace(0, 9, 100)
    pl.plot(X, f(X), '--')


.. plot:: pyplots/demo_interpolate.py

Interlude
==========

.. |tarek| image:: tarek.jpg
    :scale: 150

.. |lena| image:: lena.png
    :scale: 45

.. htmlonly::

    |tarek| |lena|

.. literalinclude:: interlude_displayed.py

.. plot:: pyplots/interlude.py

Lineaire Algebra
=================

"whitening" Lena::

    rows, weight, columns = np.linalg.svd(l, full_matrices=False)
    l_ = np.dot(rows, columns)

.. plot:: pyplots/lena_whitened.py


FFT
=====

Low pass filtering:

.. plot:: pyplots/demo_fft.py
    :include-source:

Signal processing
==================

* Detrend:

 .. plot:: pyplots/demo_detrend.py
    :include-source:


* Filtering:

  ================== ===============================================
  ================== ===============================================
  Ground truth:       ::
                        
                        l = sp.lena()[200:-100, 150:-150]
                        l = l/float(l.max())

  Noisy observation:  ::
                        
                        g = l + .1*np.random.normal(size=l.shape)
  ================== ===============================================

    .. plot:: pyplots/demo_filtering1.py

  ================== ===============================================
  ================== ===============================================
  Gaussian filter:    ::
                        
                        ndimage.gaussian_filter(g, 1.6)

  Median filter:      ::
                        
                        signal.medfilt2d(g, 5)

  Wiener filter:      ::

                        signal.wiener(g, (5, 5))

  ================== ===============================================

    .. plot:: pyplots/demo_filtering2.py

