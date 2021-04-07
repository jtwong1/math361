# Euler's method (scalar ODE) example code
import numpy as np
import matplotlib.pyplot as plt


def fwd_euler(f, a, b, y0, h):
    """ Forward Euler with fixed step size using a while loop.
        Args:
            f - the ODE function (y' = f(t,y)), a function of two variables
            a,b - the interval of integration (from a up to b)
            y0  - initial value y(a) = y0
            h - step size (fixed)
        Returns:
            tvals - list of grid points (t0, t1, ...)
            yvals - solution approximation at tvals
    """
    y = y0
    yvals = [y]
    tvals = [a]
    t = a  # set current time
    while t + h < b + 1e-12:  # (avoids rounding error where t misses b slightly)
        y += h*f(t, y)
        t += h
        yvals.append(y)
        tvals.append(t)

    return tvals, yvals


def ode_func(t, y):
    """ ode function: (y' = 2ty) """
    return 2*t*y


def sol_true(t, y0):
    """ true solution for the example, given y(0) = y0 """
    return y0*np.exp(t**2)


if __name__ == "__main__":
    """ Solve y' = 2ty, y(0) = 1 using Euler's method.
        (Example from lecture with a plot)
    """
    b = 1
    h = 0.05
    y0 = 1
    t, y_approx = fwd_euler(ode_func, 0, b, y0, h)

    # example print at t=b
    print("t=b: {:.2f} (exact) \t {:.2f} (approx)".format(t[-1], y_approx[-1]))

    # (you can vectorize this; written out to illustrate calculation)
    max_error = 0
    for k in range(len(y_approx)):
        max_error = max(max_error, abs(y_approx[k] - sol_true(t[k], y0)))
    print("h={:.4f}... max error in [0,b]: {:.2e}".format(h, max_error))

    t_true = np.linspace(0, b, 200)  # use a finer grid to plot true solution
    y_true = sol_true(t_true, y0)  # use numpy vector math
    plt.figure()
    plt.plot(t, y_approx, '.--r')
    plt.plot(t_true, y_true, '-k')
