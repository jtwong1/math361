"""
Homework 3 template code: LU factorization
(I've also included some examples of creating matrices in python. You can
 pick the method that you prefer. Note that you're free to use either
 python lists of lists OR numpy arrays for your matrices.')

 The __main__ includes an example of use for scipy's built in solver,
 which you can use to check your answer.

 Note that you can rename the variables (e.g. a, u) if you prefer longer names,
 and you may need to adjust depending on your choice of numpy array vs list.
"""

import numpy as np


def lu_factor(a):
    """ computes the LU factorization of a using Gaussian elimination;
        returns a new matrix containing L and U.
        Args:
            a: the matrix to factor
        Returns:
            u : L and U, stored compactly in the lower/upper halves
    """
    # create a copy of of the matrix first for reduction.
    # note that the way you do this depends on the type you are using!
    # u = (make a copy of a)

    # ... reduce u and construct L...

    return u


def fwd_solve_lu(a, b):
    """ Solves Lx = b where L is stored in the lower half of a """
    n = len(b)
    x = [0]*n  # or replace with np.array (x = np.zeros(n))
    for i in range(n):
        x[i] = b[i]
        for j in range(0, i):
            x[i] -= a[i][j]*x[j]
    return x


def back_solve_lu(a, b):
    """ Solves Ux = b where U is stored in the upper half of a """
    n = len(b)
    x = [0]*n  # or a np.array (x = np.zeros(n))
    # ...
    return x


def linsolve(a, b):
    """ Solves the linear system Ax = b using Gaussian elimination.
        Args:
            a: ... (fill in, specifying the type of a)
            b: ...
        Returns:
            x: ...
    """
    # compute LU factorization
    # solve Ly = b
    # solve Ux = y
    return x


if __name__ == '__main__':

    # examples of matrix construction
    # [do not retain all of this example code in submission!!]

    # version 1: list of rows
    a = [[6, -4, 2], [-2, 2, -1], [2, -2, 2]]
    b = [1, 0, 1]

    # version 2: initialize numpy arrays (also from lists)
    # (note: force type to float to clarify,
    # since elements are integers as written)
    a2 = np.array([[6, -4, 2], [-2, 2, -1], [2, -2, 2]], dtype=float)
    b2 = np.array([1, 0, 1], dtype=float)

    # version 3: initialize space, set elements piece by biece
    a3 = np.zeros((3, 3))  # 2d numpy array
    a3[0, :] = [6, -4, 2]  # ... by row ...
    a3[1, :] = [-2, 2, -1]
    a3[2, 0] = 2  # ... one element at a time...
    a3[2, 1] = -2
    a3[2, 2] = 2

    x = np.linalg.solve(a, b)  # example of numpy's solver
    x2 = np.linalg.solve(a2, b2)  # (works with lists or numpy arrays)
    print(x)
