""" HW 1 solution example code: bisection
    Note: you may have different stylistic choices; while intended
    to be "model" code there are variations that are also reasonable or better!
"""
import numpy as np
from numpy import sign


def find_zero(func, a, b, tol):
    """ Estimates the solution to f(x) = 0 using bisection.
        Inputs:
            func - the function f(x)
            a, b - endpoints of initial bracketing interval
            tol - abs. error bound to achieve.
        Outputs:
            x - the approximation
            it - number of iterations taken
            seq - the sequence of approximations [for testing]
    """

    fa = func(a)
    fb = func(b)

    if sign(fa)*sign(fb) > 0:
        raise ValueError("Signs of f at endpoints must differ!")

    it = 0
    seq = []

    while b-a > tol:
        c = 0.5*(a + b)
        seq.append(c)
        fc = func(c)  # (one function evaluation per step!)

        if abs(fc) < 1e-40:
            b = a  # force end of while loop
        elif sign(fa)*sign(fc) < 0:
            b = c
        else:
            a = c
            fa = fc

        it += 1

    return c, it, seq


def func(x):
    return x**3 - 8


# Answers:
# error bound suggests 13 iterations are required
# the actual number required with initial interval [1.6, 2.6] is 10
# as shown in the table output (err: 9.8e-5 for n=10)
#
# in general, the bound can be much greater than the actual error.

if __name__ == "__main__":
    exact = 2
    c, it, seq = find_zero(func, 1.6, 2.6, tol=1e-4)

    print("1. With  interval [1.6, 2.6]:")
    print("iter \t x \t\t err")
    for k in range(it):
        err = abs(exact - seq[k])
        print("{} \t {:.6f} \t {:.2e}".format(k, seq[k], err))

    c, it, seq = find_zero(func, 1.5, 2.5, tol=1e-4)
    print("\n2. with centered interval: ", seq, " ({} iteration)".format(it))
