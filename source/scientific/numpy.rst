===================================
Numpy: array computing
===================================

.. topic:: Conventions
    
    ::

     >>> import numpy as np
     >>> import scipy as sp
     >>> import pylab as pl


Array computing
============================

    +--------------------------+-------------------------------------+
    | Python                   | numpy                               |
    +--------------------------+-------------------------------------+
    | List:  `a = [1, 2, 3]`   | Array:    `a = np.array([1, 2, 3])` |
    +--------------------------+-------------------------------------+

Doing operations on many numbers
---------------------------------------------

* Standard numerical computing = loops

  ::

    def square(data):
        for i in range(len(data)):
            data[i] = data[i]**2
        return data

  .. sourcecode:: ipython

    In [1]: %timeit data = range(1000) ; square(data)
    1000 loops, best of 3: 314 us per loop


* Vector computing: loops are replaced by vector operations, on arrays

  ::

    def square(data):
        return data**2

  .. sourcecode:: ipython

    In [2]: %timeit data=np.arange(1000) ; square(data)
    100000 loops, best of 3: 10.6 us per loop


Multidimensional arrays
-----------------------------

::

    >>> a = np.arange(10)
    >>> a
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> b = np.reshape(a, (2, 5))
    >>> b
    array([[0, 1, 2, 3, 4],
           [5, 6, 7, 8, 9]])
    >>> b[:, 1]
    array([1, 6])


Creating arrays
---------------------

* With constants::

    >>> np.ones((2, 3))
    array([[ 1.,  1.,  1.],
           [ 1.,  1.,  1.]])

* Arrays contain typed entries::

    >>> np.ones(3, dtype=np.int)
    array([1, 1, 1])

* Creating a grid::

    >>> x, y = np.indices((2, 2))
    >>> x
    array([[0, 0],
           [1, 1]])
    >>> y
    array([[0, 1],
           [0, 1]])
    >>> x+1j*y
    array([[ 0.+0.j,  0.+1.j],
           [ 1.+0.j,  1.+1.j]])

Views and copies
--------------------

::

    >>> x = np.zeros(10)
    array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])
    >>> x[0] = 1
    >>> x
    array([ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])
    >>> y = x.copy()
    >>> y[0] = 2
    >>> x
    array([ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])


Slicing
---------

Multidimensional traversing of arrays

.. image:: numpy_indexing.png
   :align: center

An example: calculating the laplacian
----------------------------------------------

.. image:: laplacien.jpg
    :align: center

::

    image[1:-1, 1:-1] = (image[:-2, 1:-1] - image[2:, 1:-1] +
                         image[1:-1, :-2] - image[1:-1, 2:])*0.25


.. sourcecode:: ipython

    In [3]: import pylab as pl
    In [4]: l = sp.lena()
    In [5]: pl.imshow(l, cmap=pl.cm.gray())
    In [6]: e = l[:-2, 1:-1] - l[2:, 1:-1] + l[1:-1, :-2] - l[1:-1, 2:]
    In [7]: pl.imshow(e, cmap=pl.cm.gray())


.. plot:: pyplots/lena_laplacien.py 

____

.. figure:: timings.png
    :align: center

    **Timing ratio**

Advanced indexing
==================

With integers or masks

.. image:: numpy_fancy_indexing.png
   :align: center

With integer arrays
------------------------------------

.. 
   >>> np.random.seed(4)

* Example: sorting a vector with another one::

    >>> a, b = np.random.random_integers(10, size=(2, 4)) 
    >>> a
    array([8, 6, 2, 9])
    >>> b
    array([ 8,  9,  3, 10])
    >>> a_order = np.argsort(a)
    >>> a_order
    array([2, 1, 0, 3])
    >>> b[a_order]
    array([ 3,  9,  8, 10])

Using masks
-------------------------

* Zeroing out all the even elements of a table::

    >>> a = np.arange(10)
    >>> a
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> a[a % 2] = 0
    >>> a
    array([0, 0, 2, 3, 4, 5, 6, 7, 8, 9])

* Applying a mask to a grid to select the center of an image:

  .. sourcecode:: ipython

    In [8]: n, m = l.shape
    In [9]: x, y = np.indices((n, m))
    In [10]: distances = np.sqrt((x - 0.5*n)**2 + (y - 0.5*m)**2)
    In [11]: l[distance > 200] = 255
    In [12]: pl.imshow(l, cmap=pl.cm.gray)


.. plot:: pyplots/lena_mask.py 



Broadcasting
================

Multidimensional operations
-------------------------------

* You can add a numer to an array::

    >>> a = np.ones((3, ))
    >>> a
    array([ 1.,  1.,  1.])
    >>> a + 1
    array([ 2.,  2.,  2.])

* And what if we add two arrays of different shapes? ::

    >>> b = 2*np.ones((2, 1))
    >>> b
    array([[ 2.],
           [ 2.]])
    >>> a + b
    array([[ 3.,  3.,  3.],
           [ 3.,  3.,  3.]])

* Dimensions are matched:

.. image:: broadcasting.jpg
    :align: center

Using broadcasting for performance
-------------------------------------


* Creating a 3D grid

  .. image:: 3d_radius.jpg
    :align: center

  ::

    np.sqrt(x**2 + y**2 + z**2)

____

.. image:: 3d_radius_non_broadcasting.jpg
    :align: right
         

:Without broadcasting:

      .. raw:: latex

         \rule{0pt}{2em}

      ::

        >>> x, y, z = np.mgrid[-100:100, -100:100, -100:100]
        >>> print x.shape, y.shape, z.shape
        (200, 200, 200) (200, 200, 200) (200, 200, 200)
        >>> r = np.sqrt(x**2 + y**2 + z**2)

      * Timing: **2.3s**: creating `x`, `y`, `z`: 0.5s, calculation of `r`: 1.8s

      * Memory : 64Mo per array, 6 arrays,
        (`x`, `y`, `z`, `r`) and 2 temporary arrays 

        => **400Mb**

      * 200^3 floating point operations per array: 
      
        **48 million operations**.


____

.. image:: 3d_radius_broadcasting.jpg
    :align: right
         
:With broadcasting:

      .. raw:: latex

         \rule{0pt}{2em}

      ::

        >>> x, y, z = np.ogrid[-100:100, -100:100, -100:100]
        >>> print x.shape, y.shape, z.shape
        (200, 1, 1) (1, 200, 1) (1, 1, 200)
        >>> r = np.sqrt(x**2 + y**2 + z**2)

      * Timing: **1.1s**: creating `x`, `y`, `z`: 6ms

      * Memory: `x`, `y`, `z` : 1.6Kb. `r` : 64Mo, and one 64Mo temporary
        array
        
        => **120Mb**

      * **16 million operations** 

.. raw:: html

   <br\>
   &nbsp;
   <br\>

.. topic:: `numpy`: a structured view on memory, with associated operations

  * identical data type (`dtype`)
  * fast indexing
  * views and copies
  * costless reshape
  * shape-aware operations (broadcasting)


.. :vim:spell:
   :vim:spelllang=fr:

