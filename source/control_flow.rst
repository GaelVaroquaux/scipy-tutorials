Control Flow
============

Control the order in which the code is executed.

if/else
--------

.. sourcecode:: ipython
  
    In [1]: if 2**2 == 4:
       ...:         print 'Totology'
       ...: 
    Totology


**Blocks are delimited by indentation**

.. sourcecode:: ipython

    In [2]: a = 10
    
    In [3]: if a == 1:
       ...:         print 1
       ...: elif a == 2:
       ...:         print 2
       ...: else:
       ...:         print 'A lot'
       ...: 
    A lot

for/range
----------

Iterating with an index:

.. sourcecode:: ipython

    In [4]: for i in range(4):
       ...:         print i
       ...: 
    0
    1
    2
    3

But most often, it is more readable to iterate over values:

.. sourcecode:: ipython

    In [5]: for word in ('cool', 'powerful', 'readable'):
       ...:         print 'Python is', word
       ...: 
    Python is cool
    Python is powerful
    Python is readable


while/break/continue
---------------------

Typical C-style while loop (Mandelbrot problem):

.. sourcecode:: ipython

    In [6]: z = 1 + 1j

    In [7]: while abs(z) < 100:
       ...:     z = z**2 + 1
       ...:     

    In [8]: z
    Out[8]: (-134+352j)


*break* out of enclosing for/while loop:

.. sourcecode:: ipython

    In [9]: z = 1 + 1j

    In [10]: while abs(z) < 100:
       ....:     if z.imag == 0:
       ....:         break
       ....:     z = z**2 + 1
       ....:     
       ....:     


*continue* the next iteration of a loop.

.. todo:: 
   
   Add continue example.

Conditional Expressions
-----------------------

Evaluate to True:
  * any non-zero value
  * any sequence with a length > 0

Evaluate to False:
  * any zero value
  * any empty sequence


Advanced iteration
-------------------------

Iterate over any *sequence*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* You can iterate over any sequence (string, list, dictionary, file, ...)

  .. sourcecode:: ipython

    In [11]: vowels = 'aeiouy'

    In [12]: for i in 'powerful':
       ....:     if i in vowels:
       ....:         print i,
       ....:         
       ....:         
    o e u

.. warning:: Not safe to modify the sequence you are iterating over.

Keeping track of enumeration number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Common task is to iterate over a sequence while keeping track of the
item number.

* Could use while loop with a counter as above. Or a for loop:

  .. sourcecode:: ipython

    In [13]: for i in range(0, len(words)):
       ....:     print i, words[i]
       ....:     
       ....:     
    0 cool
    1 powerful
    2 readable

* But Python provides **enumerate** for this:

  .. sourcecode:: ipython

    In [14]: for index, item in enumerate(words):
       ....:     print index, item
       ....:     
       ....:     
    0 cool
    1 powerful
    2 readable

Looping over a dictionary
~~~~~~~~~~~~~~~~~~~~~~~~~~

Use **iteritems**:

.. sourcecode:: ipython

    In [15]: d = {'a': 1, 'b':1.2, 'c':1j}

    In [15]: for key, val in d.iteritems():
       ....:     print 'Key:', key, 'has value:', val
       ....:     
       ....:     
    Key: a has value: 1
    Key: c has value: 1j
    Key: b has value: 1.2

List Comprehensions
-------------------

.. todo::

   Do we want to introduce list comprehensions?

   Gael: Yes, I believe

