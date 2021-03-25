# example solution code for HW 6
# (see written solutions for the discussion)
import numpy as np
import matplotlib.pyplot as plt


def bary_weights(nodes):
    """ computes the barycentric (or mod. Lagrange)
        weights for the given nodes """
    n = len(nodes)-1
    w = [1]*(n+1)
    for i in range(0, n+1):
        for j in range(0, n+1):
            if j == i:
                continue
            w[i] /= (nodes[i] - nodes[j])  # /(xi - xj)
    return w


def bary_polyval(w, nodes, yvals, x):
    """ Computes interpolant in barycentric form """
    n = len(nodes)
    npts = len(x)
    den = [0]*npts  # denominator
    y = np.zeros(npts)  # result
    for k in range(0, npts):
        matched = False

        for i in range(n):  # check if the sample x is a node
            if abs(x[k] - nodes[i]) < 2e-16:
                y[k] = yvals[i]
                matched = True
                break

        if matched:
            continue

        for i in range(n):
            fact = w[i]/(x[k] - nodes[i])  # numerator = sum fact*f
            y[k] += yvals[i]*fact  # denominator = sum fact
            den[k] += fact

        y[k] /= den[k]

    return y


def interp(nodes, yvals, x):
    """ interpolates the given data at a set of sample points x.
        Args:
            nodes - the interpolation nodes x_i
            yvals - the data y_i at the nodes
            x - the sample points to be evaluated (float or list/array)
        Returns:
            y - the value of the interpolant at the sample points
    """

    b = bary_weights(nodes)
    if type(x) == float:  # quick fix since internal function only takes lists
        y = bary_polyval(b, nodes, yvals, [x])
        return y[0]
    else:
        y = bary_polyval(b, nodes, yvals, x)
        return y


def nice(x):
    return 1.0/(1 + x**2)


def runge(x):  # Runge's example function
    return 1.0/(1 + 25*x**2)


def error_data(func, ival, max_deg, cheby=False):
    """ computes maximum error in [a,b] of interpolant for n=1 up to max_deg
        Args:
            func: the function to interpolate [*must be vectorized]
            ival: interval as a tuple (a, b)
            max_deg: maximum degree of interpolant to test
    """
    err = [0]*max_deg

    samples = np.linspace(*ival, 10*max_deg)

    for n in range(1, max_deg + 1):
        if cheby:
            nodes = np.array([np.cos(np.pi*(2*i+1)/(2*n)) for i in range(n)])
        else:
            nodes = np.linspace(*ival, n + 1)

        yvals = func(nodes)
        f_interp = interp(nodes, yvals, samples)
        f_true = func(samples)
        err[n-1] = max(abs(f_interp - f_true))

    return err


if __name__ == '__main__':

    # ------divergence example -------
    err = error_data(runge, (-1, 1), 25)

    # table of successive ratios
    for i in range(len(err) - 5, len(err)):
        ratio = err[i]/err[i-1]
        print("{} \t {:.2e} \t r={:.3f}".format(i, err[i], ratio))

    plt.figure(1, figsize=(3.5, 3))
    nvals = np.arange(1, len(err) + 1)
    plt.semilogy(nvals, err, '.k')
    refline = np.sqrt(2)**nvals
    plt.semilogy(nvals[1:len(err)//2], refline[1:len(err)//2], '--r')
    plt.legend(["error", "slope 1.4"])
    plt.savefig("divergence_runge.pdf", bbox_inches="tight")
    plt.show()

    # ------- convergence example: chebyshev nodes -----------
    err = error_data(runge, (-1, 1), 30, cheby=True)

    plt.figure(1, figsize=(3.5, 3))
    nvals = np.arange(1, len(err) + 1)
    plt.semilogy(nvals, err, '.k')
    refline = 10*(0.82)**nvals
    plt.semilogy(nvals[len(err)//2:], refline[len(err)//2:], '--r')
    plt.legend(["error", "slope 0.82"])
    plt.savefig("convergence_cheby.pdf", bbox_inches="tight")
    plt.show()
