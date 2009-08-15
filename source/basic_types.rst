Basic types
============

Numbers
--------

* IPython as a calculator:

  .. sourcecode:: ipython

    In [1]: 1 + 1
    Out[1]: 2

    In [2]: 2**10
    Out[2]: 1024

    In [3]: (1 + 1j)*(1 - 1j)
    Out[3]: (2+0j)

* scalar types: int, float, complex

  .. sourcecode:: ipython

    In [4]: type(1)
    Out[4]: <type 'int'>

    In [5]: type(1.)
    Out[5]: <type 'float'>

    In [6]: type(1 + 0j)
    Out[6]: <type 'complex'>

.. warning:: Integer division

    .. sourcecode:: ipython

	In [7]: 3/2
	Out[7]: 1

	In [8]: from __future__ import division

	In [9]: 3/2
	Out[9]: 1.5

    **Trick:** Use floats

    .. sourcecode:: ipython

	In [10]: 3./2
	Out[10]: 1.5

* Type conversion:

  .. sourcecode:: ipython

    In [11]: float(1)
    Out[11]: 1.

Collections
------------

Collections: list, dictionaries (and tuples, sets, ...)

Lists
~~~~~~

.. sourcecode:: ipython

    In [12]: l = [1, 2, 3, 4, 5]

* Indexing:

  .. sourcecode:: ipython

    In [13]: l[2]
    Out[13]: 3

  Counting from the end:

  .. sourcecode:: ipython

    In [14]: l[-1]
    Out[14]: 5

* Slicing:

  .. sourcecode:: ipython

    In [15]: l[3:]
    Out[15]: [4, 5]

    In [16]: l[:3]
    Out[16]: [1, 2, 3]

    In [17]: l[::2]
    Out[17]: [1, 3, 5]

    In [18]: l[-3:]
    Out[18]: [3, 4, 5]

  **Syntax:** `start:stop:stride`

* Operations on lists:

  Reverse `l`:

  .. sourcecode:: ipython

    In [19]: r = l[::-1]

    In [20]: r
    Out[20]: [5, 4, 3, 2, 1]

  Append an item to `r`:

  .. sourcecode:: ipython

    In [21]: r.append(3.5)

    In [22]: r
    Out[22]: [5, 4, 3, 2, 1, 3.5]

  Sort `r`:

  .. sourcecode:: ipython

    In [23]: r.sort()

    In [24]: r
    Out[24]: [1, 2, 3, 3.5, 4, 5]

.. note:: **Methods:**
    
    `r.sort`: `sort` is a method of `r`: a special function to is applied
    to `r`.

.. warning:: **Mutables:**
    
    Lists are mutable types: `r.sort` modifies in place `r`.

Dictionaries
~~~~~~~~~~~~

Dictionaries are a mapping between keys and values:

  .. sourcecode:: ipython

    In [25]: d = {'a': 1, 'b':1.2, 'c':1j}

    In [26]: d['b']
    Out[26]: 1.2

    In [27]: d['d'] = 'd'

    In [28]: d
    Out[28]: {'a': 1, 'b': 1.2, 'c': 1j, 'd': 'd'}

    In [29]: d.keys()
    Out[29]: ['a', 'c', 'b', 'd']

    In [30]: d.values()
    Out[30]: [1, 1j, 1.2, 'd']

.. warning:: Keys are not ordered

More collection types
~~~~~~~~~~~~~~~~~~~~~

* Sets: non ordered, unique items:

  .. sourcecode:: ipython

    In [31]: s = set(('a', 'b', 'c', 'a'))

    In [32]: s
    Out[32]: set(['a', 'b', 'c'])

    In [33]: s.difference(('a', 'b'))
    Out[33]: set(['c'])

  Sets cannot be indexed:

  .. sourcecode:: ipython

    In [34]: s[1]
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)

    TypeError: 'set' object does not support indexing


* Tuples: non-mutable lists:

  .. sourcecode:: ipython

    In [35]: t = 1, 2
    
    In [36]: t
    Out[36]: (1, 2)
    
    In [37]: t[1]
    Out[37]: 2
    
    In [38]: t[1] = 2
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    
    TypeError: 'tuple' object does not support item assignment
    

