Basic types
============

Numbers
--------

* IPython as a calculator:

  .. sourcecode:: ipython

    In [4]: 1 + 1
    Out[4]: 2

    In [5]: 2**10
    Out[5]: 1024

    In [6]: (1 + 1j)*(1 - 1j)
    Out[6]: (2+0j)

* scalar types: int, float, complex

  .. sourcecode:: ipython

    In [7]: type(1)
    Out[7]: <type 'int'>

    In [8]: type(1.)
    Out[8]: <type 'float'>

    In [9]: type(1 + 0j)
    Out[9]: <type 'complex'>

.. warning:: Integer division

    .. sourcecode:: ipython

	In [10]: 3/2
	Out[10]: 1

	In [11]: from __future__ import division

	In [12]: 3/2
	Out[12]: 1.5

    **Trick:** Use floats

    .. sourcecode:: ipython

	In [13]: 3./2
	Out[13]: 1.5

* Type conversion:

  .. sourcecode:: ipython

    In [14]: float(1)
    Out[14]: 1.

Collections
------------

Collections: list, dictionaries (and tuples, sets, ...)

Lists
~~~~~~

.. sourcecode:: ipython

    In [15]: l = [1, 2, 3, 4, 5]

* Indexing:

  .. sourcecode:: ipython

    In [16]: l[2]
    Out[16]: 3

  Counting from the end:

  .. sourcecode:: ipython

    In [17]: l[-1]
    Out[17]: 5

* Slicing:

  .. sourcecode:: ipython

    In [18]: l[3:]
    Out[18]: [4, 5]

    In [19]: l[:3]
    Out[19]: [1, 2, 3]

    In [20]: l[::2]
    Out[20]: [1, 3, 5]

    In [21]: l[-3:]
    Out[21]: [3, 4, 5]

  **Syntax:** `start:stop:stride`

* Operations on lists:

  Reverse `l`:

  .. sourcecode:: ipython

    In [22]: r = l[::-1]

    In [23]: r
    Out[23]: [5, 4, 3, 2, 1]

  Append an item to `r`:

  .. sourcecode:: ipython

    In [24]: r.append(3.5)

    In [25]: r
    Out[25]: [5, 4, 3, 2, 1, 3.5]

  Sort `r`:

  .. sourcecode:: ipython

    In [26]: r.sort()

    In [27]: r
    Out[27]: [1, 2, 3, 3.5, 4, 5]

.. note:: **Methods:**
    
    `r.sort`: `sort` is a method of `r`: a special function to is applied
    to `r`.

.. warning:: **Mutables:**
    
    Lists are mutable types: `r.sort` modifies in place `r`.

Dictionaries
~~~~~~~~~~~~

Dictionaries are a mapping between keys and values:

  .. sourcecode:: ipython

    In [28]: d = {'a': 1, 'b':1.2, 'c':1j}

    In [29]: d['b']
    Out[29]: 1.2

    In [30]: d['d'] = 'd'

    In [31]: d
    Out[31]: {'a': 1, 'b': 1.2, 'c': 1j, 'd': 'd'}

    In [32]: d.keys()
    Out[32]: ['a', 'c', 'b', 'd']

    In [33]: d.values()
    Out[33]: [1, 1j, 1.2, 'd']

.. warning:: Keys are not ordered

More collection types
~~~~~~~~~~~~~~~~~~~~~

* Sets: non ordered, unique items:

  .. sourcecode:: ipython

    In [34]: s = set(('a', 'b', 'c', 'a'))

    In [35]: s
    Out[35]: set(['a', 'b', 'c'])

    In [36]: s.difference(('a', 'b'))
    Out[36]: set(['c'])

  Sets cannot be indexed:

  .. sourcecode:: ipython

    In [37]: s[1]
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)

    TypeError: 'set' object does not support indexing


* Tuples: non-mutable lists:

  .. sourcecode:: ipython

    In [38]: t = 1, 2
    
    In [39]: t
    Out[39]: (1, 2)
    
    In [40]: t[1]
    Out[40]: 2
    
    In [41]: t[1] = 2
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    
    TypeError: 'tuple' object does not support item assignment
    

