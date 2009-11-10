
.. _fancy-indexing:

Fancy indexing
===============

Rules
-------

:Indexing with integer arrays: ::

    >>> import numpy as np
    >>> a = np.arange(30).reshape((3, -1))
    >>> a
    array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
           [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])
    >>> a[:, (1, 3)]
    array([[ 1,  3],
           [11, 13],
           [21, 23]])

  Shape is given by (shape of indexing array) * slices::

    >>> a[:, ((1, 3), (2, 4))].shape
    (3, 2, 2)

  If multiple integer arrays for indexing, they are broadcasted together::

    >>> a[(1, 2), ((1, ), (2, ))]
    array([[11, 21],
           [12, 22]])

:Indexing with boolean arrays: ::

    >>> a[(a%2)==0]
    array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

  Flat shape. Slicing not used::

    >>> a[:, (a%2)==0]
    array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])


Applications
-------------

Rearranging vectors 
.....................

..
  >>> np.random.seed(4321)

We have a vector family::

    >>> vectors = np.random.randint(10, size=(4, 5))
    >>> vectors
    array([[2, 8, 2, 1, 7],
           [5, 9, 2, 4, 6],
           [0, 8, 6, 5, 3],
           [1, 1, 6, 1, 1]])


We want to rearrange them by variance::

    >>> variance = np.var(vectors, axis=0)
    >>> variance
    array([  3.5   ,  10.25  ,   4.    ,   3.1875,   5.6875])
    >>> rearranged = vectors[:, np.argsort(variance)]
    >>> np.var(rearranged, axis=0)
    array([  3.1875,   3.5   ,   4.    ,   5.6875,  10.25  ])

Bootstrapping
..............

..
  >>> np.random.seed(1234)

We have a vector `a`::

    >>> a = np.arange(20).reshape((2, 10))
    >>> a
    array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]])

We want to drawn three times 10 vectors out of `a`::

    >>> indices = np.random.randint(a.shape[-1], size=(3, 10))
    >>> indices
    array([[3, 6, 5, 4, 8, 9, 1, 7, 9, 6],
           [8, 0, 5, 0, 9, 6, 2, 0, 5, 2],
           [6, 3, 7, 0, 9, 0, 3, 2, 3, 1]])
    >>> bootstrap = a[:, indices]
    >>> bootstrap
    array([[[ 3,  6,  5,  4,  8,  9,  1,  7,  9,  6],
            [ 8,  0,  5,  0,  9,  6,  2,  0,  5,  2],
            [ 6,  3,  7,  0,  9,  0,  3,  2,  3,  1]],
    <BLANKLINE>
           [[13, 16, 15, 14, 18, 19, 11, 17, 19, 16],
            [18, 10, 15, 10, 19, 16, 12, 10, 15, 12],
            [16, 13, 17, 10, 19, 10, 13, 12, 13, 11]]])

Now we can do vectorized computations easily on the bootstraped sample.


Extracting a cut of volume along a horizon
...........................................

We have an image (volumetric data)::

    >>> image = np.random.randint(10, size=(5, 5))
    >>> image
    array([[3, 1, 3, 7, 1],
           [7, 4, 0, 5, 1],
           [5, 9, 9, 4, 0],
           [9, 8, 8, 6, 8],
           [6, 3, 1, 2, 5]])

And a horizon: the coordinates of a curve in the image::

    >>> horizon = np.array([3, 2, 1, 3, 2])

We can extract the value on the horizon::

    >>> image[horizon, np.arange(5)]
    array([9, 9, 0, 6, 0])


Local average along a horizon
...............................

This time, we want to extract the voxels in the 3-voxels-wide region
around the horizon::

    >>> image[horizon + np.arange(-1, 2)[:, np.newaxis], np.arange(5)]
    array([[5, 4, 3, 4, 1],
           [9, 9, 0, 6, 0],
           [6, 8, 9, 2, 8]])

Two broadcastings: one in x coordinates 
`horizon + np.arange(-1, 2)[:, np.newaxis]`, and the second one between
the x and the y coordinates.

____

**Drawback of these techniques: costly in memory**

