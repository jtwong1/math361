# Example code: trapezoidal rule + error (HW 8)

import numpy as np
import matplotlib.pyplot as plt


def trapz(f, a, b, n):
    """ trapezoidal rule, n sub-intervals """
    total = 0.5*(f(a) + f(b))
    h = (b-a)/n
    for k in range(1, n):
        total += f(a + k*h)
    total *= h
    return total


def func1(x):
    return np.exp(x)


def func2(x):
    return x**2*(x-1)**2*np.exp(x)


def func3(x):
    return 1/(1 + np.sin(x)**2)


def error_test(hvals, f, interval, exact):
    """ use the exact solution to calculate error, then plot it """
    width = interval[1] - interval[0]

    m = len(hvals)
    approx = np.zeros(m)
    err = np.zeros(m)
    for k in range(len(hvals)):
        approx[k] = trapz(f, *interval, int(width/hvals[k]))
        err[k] = abs(approx[k] - exact)

    return approx, err


if __name__ == "__main__":

    # Example 1: typical convergence, O(h^2)
    hvals = np.array([2**(-k) for k in range(3, 10)])
    approx, err = error_test(hvals, func1, (0, 1), np.e - 1)
    approx2, err2 = error_test(hvals, func2, (0, 1), 14*np.e - 38)

    # plot the error (log-log)
    plt.figure(figsize=(4, 3))
    plt.loglog(hvals, err, '.-k', markersize=12)
    plt.loglog(hvals, err2, '.-k', markersize=12)

    # plot a reference line
    m = len(hvals)//2
    plt.loglog(hvals[0:m], 10*hvals[0:m]**2, '--r')

    plt.xlabel('$h$')
    plt.legend(['error (a)', 'error (b)', 'slope 2'])
    plt.savefig('trapz1.pdf', bbox_inches='tight')
    plt.show()

    # Example 2: exponential convergence, O(e^{-C/h})
    nvals = np.array(range(2, 40, 2))
    hvals = 2*np.pi/nvals
    approx, err = error_test(hvals, func3, (0, 2*np.pi), np.pi*np.sqrt(2))

    # plot the error (log-log)
    plt.figure(figsize=(4, 3))
    plt.semilogy(nvals, err, '.-k', markersize=12)

    plt.xlabel('$h$')
    plt.ylabel('$err$')
    plt.savefig('trapz2.pdf', bbox_inches='tight')
    plt.show()