========================================
The workflow: IPython and a text editor 
========================================


   **Interactive work to test and understand algorithm**


Command line interaction
=========================

Start `ipython`:

.. sourcecode:: ipython

    In [1]: print('Hello world')
    Hello world


Elaboration of the algorithm in an editor
===========================================

Edit `my_file.py`::

    s = `Hello world`
    print(s) 

Run it in ipython and explore the resulting variables:

.. sourcecode:: ipython

    In [2]: %run my_file.py
    Hello word

    In [3]: s
    Out[3]: 'Hello word'

.. note:: **From a script to functions**

    * A script is not reusable, functions are.

    * Important: break the process in small blocks.


.. :vim:spell:



