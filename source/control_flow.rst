====================================
Introduction to the Python language
====================================

Control Flow
============

Control the order in which the code is executed.

if/else
--------

::
  
    if 2**2 == 4:
	print 'Totology'

**Blocks are delimited by indentation**

::

    a = 1
    if a == 1:
	print 1
    elif a == 2:
	print 2
    else:
	print 'A lot'

for/range
----------

Iterating with an index::

    for i in range(10):
	print i

But most often, it is more readable to iterate over values::

    for word in ('cool', 'powerful', 'readable'):
	print 'Python is', word

    
while/break/continue
---------------------

Typical C-style while loop:

.. sourcecode:: ipython

    In [3]: words = ('cool', 'powerful', 'readable')

    In [4]: i = 0

    In [5]: while i < len(words):
       ...:     print 'Python is', words[i]
       ...:     i += 1
       ...:     
       ...:     
    Python is cool
    Python is powerful
    Python is readable

*break* out of enclosing for/while loop:

.. sourcecode:: ipython

    In [30]: words = ['cool', 'powerful', 'readable']

    In [31]: i = 0

    In [32]: while i < len(words):
       ....:     curr_word = words[i]
       ....:     if curr_word == 'powerful':
       ....:         print curr_word.upper()
       ....:         break
       ....:     print curr_word
       ....:     i += 1
       ....: 
    cool
    POWERFUL

*continue* the next iteration of a loop:

Conditional Expressions
-----------------------

Evaluate to True:
  * any non-zero value
  * any sequence with a length > 0

Evaluate to False:
  * any zero value
  * any empty sequence


Iterate over any *sequence*
---------------------------

You can iterate over any sequence (string, list, dictionary, file, ...)

.. sourcecode:: ipython

    In [50]: for i in 'powerful':
       ....:     if i in vowels:
       ....:         print i,
       ....:         
       ....:         
    o e u

.. warning:: Not safe to modify the sequence you are iterating over.

Common task is to iterate over a sequence while keeping track of the
item number.

Could use while loop with a counter as above. Or a for loop:

.. sourcecode:: ipython

    In [52]: for i in range(0, len(words)):
       ....:     print i, words[i]
       ....:     
       ....:     
    0 cool
    1 powerful
    2 readable

But Python provides **enumerate** for this:

.. sourcecode:: ipython

    In [53]: for i, item in enumerate(words):
       ....:     print i, item
       ....:     
       ....:     
    0 cool
    1 powerful
    2 readable

Looping over a dictionary, use *iteritems*.

Looping over a sequence and want index and value use *enumerate*.

