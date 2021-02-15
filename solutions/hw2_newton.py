""" hw2 solution code.
"""
import numpy as np
import matplotlib.pyplot as plt


def root_newton(f, df, x, tol, max_iter=50):
    """ Finds a root of f(x) given f and its derivative (df). Returns the whole
        sequence for testing (to be efficient, would only return the result).

        Args:
            f, df: the function and its derivative
            x: initial guess
            tol: absolute error tolerance

        Returns:
            x: the approximate root
            it: the number of iterations taken
            seq: the sequence of iterates
    """

    seq = [x]  # python's list is better at appending than the np list
    it = 0

    delta = np.Inf

    while it <= max_iter and abs(delta) > tol:
        dfx = df(x)
        if np.abs(dfx) < 1e-40:
            raise ValueError('Bad derivative (zero)!')

        delta = -f(x)/dfx
        x += delta
        it += 1
        seq.append(x)

    return x, it, np.array(seq)


def func3(x):
    return (x-1)**(1.5) + x - 1


def dfunc3(x):
    return 1.5*(x-1)**(0.5) + 1


def func4(x):
    return np.tan(x) - 0.5*x


def dfunc4(x):
    return np.cos(x)**(-2)


def eigenvalues(kmax):
    eigs = [0]*kmax
    it = [0]*kmax
    for k in range(kmax):
        x0 = (k+1)*np.pi + np.pi/2 - 10**(-(k+1))
        eigs[k], it[k], seq = root_newton(func4, dfunc4, x0, 1e-10)

    return eigs, it


if __name__ == '__main__':

    # ---- Problem C3 ----
    exact = 1.0
    x, it, seq = root_newton(func3, dfunc3, 2.0, 1e-10)
    print('C2b: Newton ans/iter: {:.16f} in {} iterations.'.format(x, it))
    print('Abs. error: {:.3e}'.format(abs(seq[-1]-exact)))

    errs = abs(seq - exact)
    err_n = errs[1:-1]  # e_n
    err_np1 = errs[2:]  # e_(n+1)
    ref = 10*err_n**(1.5)  # for reference line of given slope

    plt.figure(figsize=(3.5, 3))
    plt.loglog(err_n, errs[2:], '.k-', err_n, ref, '--r', markersize=12)
    plt.rc('text', usetex=True)  # enable TeX rendering for fancy plotting
    plt.title('error trend for C3')
    plt.xlabel('$\epsilon_n$')
    plt.ylabel('$\epsilon_{n+1}$')
    plt.legend(["$\epsilon_{n+1}$", "slope 3/2"])
    plt.savefig('hw2_c3.pdf', bbox_inches='tight')
    plt.show()

    # ---- Problem C4 ----
    kmax = 4
    eigs, it = eigenvalues(kmax)
    for k in range(kmax):
        print("lambda_{} = {:.10f} \t it={}".format(k+1, eigs[k], it[k]))
