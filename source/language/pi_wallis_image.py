"""Render the Wallis formula for computing pi to a png image.
"""

import matplotlib.mathtext as mathtext
import matplotlib
matplotlib.rc('image', origin='upper')

parser = mathtext.MathTextParser("Bitmap")

parser.to_png('pi_formula.png',
              r'$\pi = 2\prod_{i=1}^\infty \frac{4 i^2}{4 i^2 - 1}$',
              fontsize=24, dpi=120)

