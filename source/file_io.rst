==============================================
Introduction to the Python language (File I/O)
==============================================

Use the build-in function ``open`` to open files:

.. sourcecode:: ipython

    In [67]: fp = open("datafile.txt")

    In [68]: fp
    Out[68]: <open file 'datafile.txt', mode 'r' at 0xea1ec0>

    In [69]: fp.
    fp.__class__         fp.__new__           fp.fileno            fp.readline
    fp.__delattr__       fp.__reduce__        fp.flush             fp.readlines
    fp.__doc__           fp.__reduce_ex__     fp.isatty            fp.seek
    fp.__enter__         fp.__repr__          fp.mode              fp.softspace
    fp.__exit__          fp.__setattr__       fp.name              fp.tell
    fp.__getattribute__  fp.__str__           fp.newlines          fp.truncate
    fp.__hash__          fp.close             fp.next              fp.write
    fp.__init__          fp.closed            fp.read              fp.writelines
    fp.__iter__          fp.encoding          fp.readinto          fp.xreadlines

Close a file with the ``close`` method:

.. sourcecode:: ipython

    In [73]: fp.close()

    In [74]: fp.closed
    Out[74]: True

Can read one line at a time:

.. sourcecode:: ipython

    In [69]: first_line = fp.readline()

    In [70]: first_line
    Out[70]: "GUARD: 'Allo, daffy English kaniggets and Monsieur Arthur-King, who is\n"

Or we can read the entire file into a list:

.. sourcecode:: ipython

    In [75]: fp = open("datafile.txt")

    In [76]: all_lines = fp.readli
    fp.readline   fp.readlines  

    In [76]: all_lines = fp.readlines()

    In [77]: all_lines
    Out[77]: 
    ["GUARD: 'Allo, daffy English kaniggets and Monsieur Arthur-King, who is\n",
     '      afraid of a duck, you know!  So, we French fellows out-wit you a\n',
     '      second time!\n',
     ' \n',
    ...
     ' \n']

    In [78]: all_lines[0]
    Out[78]: "GUARD: 'Allo, daffy English kaniggets and Monsieur Arthur-King, who is\n"

Often want to open the file, grab the data, then close the file:

.. sourcecode:: ipython

    In [54]: fp = open("datafile.txt")

    In [60]: try:
       ....:     for line in fp:
       ....:         print line
       ....: finally:
       ....:     fp.close()
       ....: 
    GUARD: 'Allo, daffy English kaniggets and Monsieur Arthur-King, who is

          afraid of a duck, you know!  So, we French fellows out-wit you a

          second time!

With Python 2.5 use the ``with`` statement:

.. sourcecode:: ipython

    In [65]: from __future__ import with_statement 

    In [66]: with open('datafile.txt') as fp:
       ....:     for line in fp:
       ....:         print line
       ....: 
    GUARD: 'Allo, daffy English kaniggets and Monsieur Arthur-King, who is

          afraid of a duck, you know!  So, we French fellows out-wit you a

          second time!

This has the advantage that it closed the file properly, even if an
exception is raised, and is more concise than the ``try-finally``.

.. note::

   The ``from __future__`` line isn't required in Python 2.6


user input
----------

.. todo:: small note about ``raw_input``

.. sourcecode:: ipython

    In [77]: s = raw_input('--> ')
    --> Monty Python's Flying Circus
    In [78]: s
    "Monty Python's Flying Circus"


