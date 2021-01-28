""" HW 1 template code: bisection
    NOTE 1: when implementing your code, I recommend starting with a fresh
    document and copy/pasting sections as you need them. Please *do not*
    retain the temporary comments I have added like this that are just
    to explain the template; use your own.
"""
import numpy as np
from numpy import sign


# Fill in the doc string for bisection; you can use a different format
# if you want as long as it has the right information and isn't too long.
def find_zero(func, a, b, tol):
    """ One sentence explanation of your algorithm.
        Inputs:
            foo - short description
            bar - short description
        Outputs:
            blah - short description
            blah - short description
    """
    if sign(func(a))*sign(func(b)) > 0:
        raise ValueError("Error message goes here.")

    it = 0

    while 0.5*(b-a) > tol:
        c = 0.5*(a + b)

        if sign(func(a))*sign(func(c)) < 0:
            b = c
        elif sign(func(c))*sign(func(b)) < 0:
            a = c

        it += 1

    return c, it


# you could just use np.sin here, but in general you have to define a function
def func(x):
    return np.sin(x)


if __name__ == "__main__":
    # ... testing code goes here ....
    # some bisection examples
    c, it = find_zero(func, -0.5, 1, tol=1e-3)
    print(c, it)  # use formatted output here!
