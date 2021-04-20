# quick example for a stiff equation

import numpy as np
import matplotlib.pyplot as plt
from numpy import cos, sin, exp


def fwd_euler(f, a, b, y0, h):
    """ Forward Euler with fixed step size using a while loop."""
    y = y0
    t = a
    yvals = [y]
    tvals = [t]
    while t < b - 1e-12:  # why the 1e-12?
        y += h*f(t, y)
        t += h
        yvals.append(y)
        tvals.append(t)

    return tvals, yvals


def newton(f, df, x0, tol, max_iter=50, tolf=1e-20):
    x = x0
    it = 0
    err = 2*tol
    while it < max_iter and err > tol:
        fx = f(x)
        delta = -fx/df(x)
        x += delta
        it += 1
        err = abs(delta)
    return x, it


def back_euler(func, dfunc, a, b, y0, h, ntol=1e-10, max_iter=50):
    """ Backward Euler with fixed time step h using a while loop."""
    y = y0
    t = a
    yvals = [y]
    tvals = [t]
    while t < b - 1e-12:
        t += h
        nfunc = lambda z: z - h*func(t, z) - y  # G(z) for solving G(z) = 0
        df = lambda z: 1 - h*dfunc(t, z)  # G'(z)
        y, it = newton(nfunc, df, y, ntol, max_iter)  # get u_{n+1}
        yvals.append(y)
        tvals.append(t)

    return tvals, yvals


def exact1(t, y0, r, a=0):
    c = exp(r*a)*(y0 - sin(a))
    return sin(t) + c*exp(-r*t)


def stiff_plot(h, r, a=0, b=2, y_zero=1, fwd=True, back=False):
    def ode_func(t, y):
        return -r*(y - sin(t)) + cos(t)

    def ode_dfunc(t, y):
        return -r

    y0 = exact1(a, y_zero, r)
    t, y = fwd_euler(ode_func, a, b, y0, h)
    tex = np.linspace(0, b, 200)
    yex = exact1(tex, y_zero, r)

    plt.figure(figsize=(6, 5))

    if fwd:
        plt.plot(t, y, '--r')

    if back:
        t2, y2 = back_euler(ode_func, ode_dfunc, a, b, y0, h)
        plt.plot(t2, y2, '--b')

    plt.plot(tex, yex, '-k', a, y0, '.r', markersize=14)
    plt.title(f'h={h:.3f}')
    plt.ylim([-0.75, 2])


if __name__ == "__main__":

    # illustrates stiffness as in lecture
    r = 20
    #stiff_plot(0.09, r)
    #stiff_plot(0.08, r)

    # illustrates stiffness w/o transient
    #stiff_plot(0.11, r, b=4, y_zero=0)
    stiff_plot(0.08, r, b=4, y_zero=0)

    # illustrates backward euler
    # stiff_plot(0.2, r, y_zero=1, fwd=False, back=True)
    # stiff_plot(0.08, r, y_zero=1, fwd=False, back=True)
