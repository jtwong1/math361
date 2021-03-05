# example solution code for HW 4
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

    factors[0, 1] = A[0, 1]
    factors[0, 2] = A[0, 2]
    for k in range(1, n):
        factors[k, 0] = A[k, 0]/factors[k-1, 1]
        factors[k, 1] = A[k, 1] - factors[k, 0]*A[k-1, 2]
        factors[k, 2] = A[k, 2]

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

    # forward solve (Ly = b)
    x[0] = b[0]
    for k in range(1, n):
        x[k] = b[k] - factors[k, 0]*x[k-1]

    # backward solve (Ux = y)
    x[n-1] /= factors[n-1, 1]
    for k in range(n-2, -1, -1):
        x[k] = (x[k] - factors[k, 2]*x[k+1])/factors[k, 1]

    return x


def diff_data(n):
    """ construct the matrix/rhs for the example solve in banded form """
    mat = np.zeros((n, 3))
    b = np.zeros(n)
    for k in range(n):
        mat[k, 0] = -1  # a_(k,k-1)
        mat[k, 1] = 2  # a_(k,k)
        mat[k, 2] = -1  # a_(k,k+1)
        b[k] = (k+1)/(n+1)**3

    mat[0, 0] = 0
    mat[n-1, 2] = 0

    return mat, b


if __name__ == '__main__':

    n = 400
    a, b = diff_data(n)

    x = trisolve(a, b)
    print("inf norm of x: {:.6f}".format(max(abs(x))))

    # for comparison, check with dense matrix solve + python built in
    if n <= 1000:
        mat = np.zeros((n, n))
        mat[0, 0] = 2
        mat[0, 1] = -1
        mat[n-1, -2] = -1
        mat[n-1, n-1] = 2
        for k in range(1, n-1):
            mat[k][k-1] = -1
            mat[k][k] = 2
            mat[k][k+1] = -1

        x2 = np.linalg.solve(mat, b)  # for comparison
        print("inf norm of x2: {:.6f}".format(max(abs(x2))))
