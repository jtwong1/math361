"""Vectorization (in numpy) and append vs. pre-allocation example.
    Calculates x*sin(x) for a large number of x's.

     - Note that the vectorized operation is much faster than a for loop.
     - Appending tends to be a bit slower than pre-allocating.
     - the numpy array append is *extremely slow* (its not recommended for use)
"""

import numpy as np
from time import perf_counter as timer

if __name__ == '__main__':

    nvals = 10**6
    print("computation for {} values: \n".format(nvals))

    # 1. vectorized calculation using numpy arrays

    x = np.linspace(0.0, 1.0, nvals)
    start = timer()
    y = np.sin(x)*x  # np arith. operations are vectorized!
    end = timer()
    print('vectorized time: {:.4} s\n'.format(end-start))

    # 2. not vectorized; using a for loop but pre-allocating space
    start = timer()
    y = np.zeros(nvals)
    for n in range(0, nvals):  # for loop is slower than vectorized version
        y[n] = np.sin(x[n])*x[n]
    end = timer()
    print('for loop time: {:.4} s\n'.format(end-start))

    # 3. not vectorized; growing a python list per iteration
    start = timer()
    y = []
    for n in range(0, nvals):  # append for python lists is fast...
        y.append(np.sin(x[n])*x[n])

    end = timer()
    print('python list append time: {:.4} s\n'.format(end-start))

    # 4. not vectorized; growing a numpy array (AVOID THIS!)
    # (numpy arrays are not intended to be variable size)
    nvals = 50000
    start = timer()
    y = np.array([])
    for n in range(0, nvals):  # ... but append for numpy arrays is NOT FAST
        y = np.append(y, np.sin(x[n])*x[n])
    end = timer()
    print('np.append time (for n={}): {:.4} s\n'.format(nvals, end-start))
