

Views and strides
==================

.. _views-and-copies:

Views and copies
-----------------

Views
.......

Two arrays can point to the same data::

    >>> import numpy as np
    >>> a = np.arange(10)
    >>> a
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> b = a[3:7]
    >>> b
    array([3, 4, 5, 6])
    >>> b[0] = 0
    >>> b
    array([0, 4, 5, 6])
    >>> a
    array([0, 1, 2, 0, 4, 5, 6, 7, 8, 9])
    
`a` was also modified.

**No memory duplication**

How to tell: inspecting the data buffer
........................................

* ::

    >>> np.may_share_memory(a, b)
    True

* The `base` attribute of the array::

    >>> b.base is a
    True

* Look at the base pointer of the data buffer, and the extent::

    a.ctypes.data
    140052096
    a.ctypes.data + len(a.data)
    140052136
    b.ctypes.data
    140052108
    b.ctypes.data + len(b.data)
    140052124

* Look at the 'OWNDATA' flag to tell if the array owns its data::

    >>> b.flags
      C_CONTIGUOUS : True
      F_CONTIGUOUS : True
      OWNDATA : False
      WRITEABLE : True
      ALIGNED : True
      UPDATEIFCOPY : False

  But this does not mean another array shares the data::

    >>> del a
    >>> b.flags
      C_CONTIGUOUS : True
      F_CONTIGUOUS : True
      OWNDATA : False
      WRITEABLE : True
      ALIGNED : True
      UPDATEIFCOPY : False

  The base data container is not cleared as long as there are views opened
  on it.    

Applications
.............

* **With a mask:** ::

      >>> a = np.arange(10)
      >>> a
      array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
      >>> a[(a % 2) == 0] = 0
      >>> a
      array([0, 1, 0, 3, 0, 5, 0, 7, 0, 9])

  A view was created: an array of shape (5, ), and all the elements
  were set to zero (through :ref:`broadcasting` of 0 to a (5, )-shaped
  array).

* **In loops:** ::

    >>> a = np.arange(30).reshape((3, 10))
    >>> a
    array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
           [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])
    >>> from scipy.signal import detrend
    >>> for line in a:
    ...     line[:] = detrend(line)
    >>> a
    array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

.. _reshaping-striding:

Reshaping, striding
--------------------

Reshaping can be a special case of views.

.. Some initialization code for the code below to run in the doctests
   >>> x, y = np.ogrid[0:10, 0:10]
   >>> r = np.sqrt(x**2 + y**2)

..

* You can do unusual operations on arrays along certain strides:

  .. plot:: reshape_bin.py
      :include-source:
      :hide-links:
      :scale: 50
      :align: left 


* To understand this better, let us consider what happens to the first
  line::

    >>> r[:, 0]
    array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.])
    >>> r[:, 0].reshape((5, 2))
    array([[ 0.,  1.],
           [ 2.,  3.],
           [ 4.,  5.],
           [ 6.,  7.],
           [ 8.,  9.]])
    >>> r[:, 0].reshape((5, 2)).sum(axis=-1)
    array([  1.,   5.,   9.,  13.,  17.])

* Reshaping is (when possible) just a matter of changing the stride and
  shape for a flat array::

    >>> r = np.arange(8)
    >>> r.strides
    (4,)
    >>> r.shape
    (8,)

  ..

   .. image:: ndarray_stride_shape_1.png

  After reshape::

    >>> r2 = r.reshape((4, 2))
    >>> r2.strides
    (8, 4)
    >>> r2.shape
    (4, 2)

  ..

    
   .. image:: ndarray_stride_shape_2.png

  And when slicing backwards::

    >>> r3 = r[::-1]
    >>> r3.strides
    (-4,)


.. topic:: Take home message:

    You can apply operations with 'a certain regularity' on an array by
    finding the view that gives you the right striding and shape.


In place operations
--------------------

* Inplace operators (`*=`)

* All ufuncs take an out arguments.

:Without inplace operations: ::

    >>> x = np.linspace(-100, 100, 1e6)
    >>> y = np.linspace(-100, 100, 1e6)
    >>> r = np.sqrt(x**2 + y**2)

  Time of the calculation of `r`: **2s**

..

:Using inplace operations:

  All `ufunc` take an `out` argument::

    >>> x **= 2
    >>> y **= 2
    >>> x += y
    >>> r = np.sqrt(x, x)

  Total time: **1.4s**
  
  Memory consumption twice as small.

____

.. topic:: In conclusion: 

    **views (eventually strided) avoid memory consumption, and open the 
    door to interesting array manipulations**



