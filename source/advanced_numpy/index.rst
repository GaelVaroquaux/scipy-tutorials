Advanced numpy
==========================================

.. topic:: **Optimising numpy code**

    1) avoiding loops

    2) algorithmic optimisation (eg. not doing the same thing more than
       once)

    3) memory/number of operations minimization and trade-off


:Avoiding loops:

    * :ref:`fancy-indexing`

    * Know the numpy library well

    * :ref:`reshaping-striding`

    * Think different


:Algorithmic optimisation:

    * See the forest, not the trees:

        * Think before you code
        * Refactor

    * Know the standard scientific library (scipy)

      * http://docs.scipy.org/

      * `numpy.lookfor`

    * Know your math:

      **wrong**::

         import numpy as np
         _, singular_values, _ = np.linalg.svd(np.dot(X.T, X))

      **harder, better, faster stronger**::

         from scipy import linalg
         singular_values = sp.linalg.eigvalsh(np.dot(X.T, X))


:Minimize memory/number of operations:

    * :ref:`views-and-copies`

    * :ref:`broadcasting`

    * :ref:`fancy-indexing`

__________

**Table of Contents**

.. toctree::
    :maxdepth: 2

    broadcasting.rst
    views_and_strides.rst
    fancy_indexing.rst
    bonus.rst

..
  Indices and tables
  ==================
..
  * :ref:`genindex`
  * :ref:`modindex`
  * :ref:`search`

