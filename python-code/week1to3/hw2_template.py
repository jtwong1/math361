""" HW 2 template code:
    - newton's method
    - example for the reivew problem.
"""

import numpy as np
import matplotlib.pyplot as plt


def make_2d_array():
    """ quick example for review: creating 2d arrays and indexing. """

    # version 1: list of lists (rows)
    v1 = [[0 for j in range(3)] for k in range(3)]

    # version 2: numpy array
    v2 = np.zeros((3, 3))

    # slight variation on v1:
    v3 = [[0]*3 for k in range(3)]

    # note indexing scheme differs for nump arrays
    print("(1,1) element: {}, {}", v1[1][1], v2[1, 1])
    return v1, v2, v3


def newton(f, df, x, tol, max_iter=50):
    """ ...
        Inputs:
            ...

        Returns:
            x: the approximate root
            it: the number of iterations taken
            seq: the sequence of iterates
    """
    it = 0  # (you can rename these; placeholder values)
    seq = [1, 2, 3, 4]

    while False:
        pass  # ...newton's method here...

    return x, it, seq


def func(x):
    return x**3 - 2


def dfunc(x):
    return 3*x**2


if __name__ == '__main__':

    # ---- Problem C2b ----
    exact = 2**(1.0/3)
    x0 = 1
    x, it, seq = newton(func, dfunc, x0, 1e-12)

    plt.figure(figsize=(3.5, 3))  # plot size is in inches
    nvals = np.arange(0, len(seq))
    plt.plot(nvals, seq, '.-k', markersize=8)
    # see plotting example for formatting info
    # note that the log-log plot command is plt.loglog(...)
    # (use that to ensure the output has a nice size/format when submitting)
    # (the figure is submitted with the written portion's pdf)

    # placeholder print statement
    print('answer: {:.16f} in {} iterations.'.format(x, it))
