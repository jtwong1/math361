# solution template for HW 4; use as needed
# sketch for the lusolve structure
# example from (iii) constructed in banded form

import numpy as np


def trilu(A):
    """ ...

        Args:
            A: the input matrix as an nx3 array of bands

        Returns:
            factors: the lu decomposition, also as an nx3 array with the first
                column containing the lower diag. of L and the other two
                columns containing the central/upper diagonals of U.
    """
    n = A.shape[0]
    factors = np.zeros((n, 3))

    return factors


def trisolve(A, b):
    """ ...

        Args:
            A: the input matrix as an nx3 array of bands
            b: the RHS vector (length n)

        Returns:
            x: the solution to Ax = b
    """

    factors = trilu(A)
    n = A.shape[0]
    x = np.zeros(n)

    # forward/back solves

    return x


def diff_matrix(n):
    """ construct the matrix for the example solve in banded form """
    mat = np.zeros((n, 3))
    for k in range(n):
        mat[k, 0] = -1  # a_(k,k-1)
        mat[k, 0] = 2  # a_(k,k)
        mat[k, 0] = -1  # a_(k,k+1)

    # REMARK: the upper left/ lower right entries are *unused*,
    # so diff[0, 0] and diff[n-1, 2] could have any value.
    # It's nice to set them to zero here for clarity:

    mat[0, 0] = 0
    mat[n-1, 2] = 0

    return mat


if __name__ == '__main__':

    n = 20  # increase to a much larger number!
    a = diff_matrix(n)
    # ...
    # ... solve and output max |x_i| as before ...
