import numpy as np


def fd_center(f, h, x0):
    """ two point centered difference """
    return (f(x0 + h) - 2*f(x0) + f(x0 - h))/(h**2)


def extrap_h2_table(formula, f, h, x0, k):
    """returns the full table of approximations
        for the series c2 h^2 + c4 h^4 + ...
        starting with the base value h and function f
        and using h, h/2 ... h/2^(k-1)
         plus error estimates """
    r = [[0]*k for i in range(k)]

    # populate first column
    for i in range(k):
        r[0][i] = formula(f, h/(2**i), x0)

    errs = [0 for i in range(k)]

    errs[0] = abs((4.0/3)*(r[0][0] - r[0][1]))

    for col in range(1, k):
        for i in range(0, k-col):
            a1 = r[col-1][i]  # A(h/2^i)
            a2 = r[col-1][i+1]  # A(h/2^(i+1))
            r[col][i] = ((4**col)*a2 - a1)/(4**col - 1)
        if col < k-1:
            errs[col] = abs((4.0**(col+1)/(4.0**(col+1)-1))*(r[col][0] - r[col][1]))

    return r, errs


def func(x):
    return np.exp(2*x)


if __name__ == '__main__':

    # Richardson extrapolation example
    x0 = 1
    h = 1  # starting value of h
    exact = 4*np.e**2
    r, errs = extrap_h2_table(fd_center, func, h, x0, 8)
    true_err = [abs(r[k][0] - exact) for k in range(len(r))]
    np.set_printoptions(precision=4)
    print(np.array(r).transpose())  # use numpy's print formatting
    np.set_printoptions(precision=2)
    print(np.array(errs))
    print(np.array(true_err))
