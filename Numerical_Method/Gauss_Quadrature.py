"""author: MadPlayer
   e_mail: kch9001@gmail.com
   Gauss 5 point quadrature
"""
import numpy as np

_t0 = -1/3 * np.power(5 + 2 * np.power(10/7, 0.5), 0.5)
_t1 = -1/3 * np.power(5 - 2 * np.power(10/7, 0.5), 0.5)
_t2 = 0.0

_c0 = (322 + 13 * np.power(70, 0.5)) / 900
_c1 = (322 - 13 * np.power(70, 0.5)) / 900
_c2 = 128 / 225

_C = np.array([_c0, _c1, _c2, _c1, _c0]);
_t = np.array([_t0, _t1, _t2, -_t1, -_t0]);

def Quadrature(func, x):
    """
    func = def func(x)
    x = numpy.arange(s, e, term)
    """
    
    size = len(x)
    ans = np.zeros(size)
    for n in range(size - 1):
        a = x[n]
        b = x[n + 1]
        ans[n + 1] += ans[n]
        tmp = func((a + b)/2 + (b - a)/2 * _t) * _C
        for i in tmp:
            ans[n + 1] += i
    return ans
