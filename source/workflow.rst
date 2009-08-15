========================================
The workflow: IPython and a text editor 
========================================


   **Interactive work to test and understand algorithm**

.. note:: Reference document for this section:

    **IPython user manual:** http://ipython.scipy.org/doc/manual/html/

Command line interaction
=========================

Start `ipython`:

.. sourcecode:: ipython

    In [1]: print('Hello world')
    Hello world

Getting help:

.. sourcecode:: ipython

    In [2]: print?
    Type:		builtin_function_or_method
    Base Class:	        <type 'builtin_function_or_method'>
    String Form:	<built-in function print>
    Namespace:	        Python builtin
    Docstring:
	print(value, ..., sep=' ', end='\n', file=sys.stdout)
	
	Prints the values to a stream, or to sys.stdout by default.
	Optional keyword arguments:
	file: a file-like object (stream); defaults to the current sys.stdout.
	sep:  string inserted between values, default a space.
	end:  string appended after the last value, default a newline.


Elaboration of the algorithm in an editor
===========================================

Edit `my_file.py`::

    s = `Hello world`
    print(s) 

Run it in ipython and explore the resulting variables:

.. sourcecode:: ipython

    In [3]: %run my_file.py
    Hello word

    In [4]: s
    Out[4]: 'Hello word'

    In [5]: %whos
    Variable   Type    Data/Info
    ----------------------------
    s          str     Hello word

____

.. note:: **From a script to functions**

    * A script is not reusable, functions are.

    * Important: break the process in small blocks.


.. :vim:spell:



