Exceptions handling in Python
==============================

Exceptions
-----------

Exceptions are raised by errors in Python:

  .. sourcecode:: ipython

    In [1]: 1/0
    ---------------------------------------------------------------------------
    ZeroDivisionError: integer division or modulo by zero

    In [2]: 1 + 'e'
    ---------------------------------------------------------------------------
    TypeError: unsupported operand type(s) for +: 'int' and 'str'

    In [3]: d = {1:1, 2:2}

    In [4]: d[3]
    ---------------------------------------------------------------------------
    KeyError: 3

    In [5]: l = [1, 2, 3]

    In [6]: l[4]
    ---------------------------------------------------------------------------
    IndexError: list index out of range

    In [7]: l.foobar
    ---------------------------------------------------------------------------
    AttributeError: 'list' object has no attribute 'foobar'

**Different types of exceptions for different errors.**

Catching exceptions
--------------------

**Better to ask for forgiveness than for permission**

Raising exceptions
------------------

