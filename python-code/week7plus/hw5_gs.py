# example solution code for HW 5
# (see written solutions for the discussion)
import numpy as np


def err_norm2(x, y):
    """ returns the 2-norm of the error between vectors x and y """
    normsq = sum(((x[k]-y[k])**2 for k in range(len(x))))
    return np.sqrt(normsq)


def norm2(x):
    normsq = sum((a**2 for a in x))
    return np.sqrt(normsq)


def gs_solve(x0, b, n, tol, max_it=500):
    x = np.array(x0)
    xprev = np.array(x0)
    n = len(x)
    upp = -1  # label upper/lower/diagonal entries for clarity in formula
    low = -1  # (not necessary, but makes the purpose of the numbers clear)
    mid = 2
    err = np.inf  # (not actually the error; really the update size)
    it = 0
    sample = []
    while err > tol*norm2(x) and it < max_it:
        xprev[:] = x[:]
        x[0] = (1/mid)*(b[0] - upp*x[1])
        for k in range(1, n-1):
            x[k] = (1/mid)*(b[k] - low*x[k-1] - upp*x[k+1])
        x[n-1] = (1/mid)*(b[n-1] - low*x[n-2])
        err = err_norm2(x, xprev)
        sample.append(x[n//2])
        it += 1

    if it >= max_it:
        print("Warning: failed to converge! err = {:.2e}".format(err))

    return x, it, sample


if __name__ == '__main__':
    n = 200
    b = np.array([i/(n+1)**3 for i in range(1, n+1)])
    x0 = np.zeros(n)
    x, it, sample = gs_solve(x0, b, n, 1e-3, 10000)
    print("Max value of |x|: {:.6f} in {} iterations".format(max(abs(x)), it))

    # calculate ratios from the data (sample at midpoint)
    r_sample = np.zeros(it)
    for k in range(2, it):
        r_sample[k] = (sample[k] - sample[k-1])/(sample[k-1] - sample[k-2])

    print("ratio values (last 4):", r_sample[-4:])
