"""
author: madplayer
e_mail: kch9001@gmail.com
"""
import numpy as np

def Integration(y, x):
    """
    y is value list
    y = f(x)
    x[i + 2] - x[i] = const
    """
    size = len(x)
    j = 0
    h = x[1] - x[0]

    if (size - 1) % 2 != 0:
        ans = np.zeros(int(size / 2)-1)
        ans_x = np.zeros(int(size / 2)-1)
        for i in range(2, size - 2, 2):
            ans[j] += h / 3 * (y[i] + 4*y[i-1] + y[i-2])
            ans[j + 1] += ans[j] 
            ans_x[j] = x[i]
            j += 1
        ans[j] += 3*h/ 8 * \
                (y[size-1] + 4*y[size-2] + 4*y[size-3] + y[size-4])
        ans_x[j] = x[size - 3]
    else:
        ans = np.zeros(int(size / 2) + 1)
        ans_x = np.zeros(int(size / 2) + 1)
        for i in range(2, size, 2):
            ans[j] += h / 3 * (y[i] + 4*y[i-1] + y[i-2])
            ans[j + 1] += ans[j] 
            ans_x[j] = x[i]
            j += 1
            ans_x[j] = x[size - 1]

    return ans, ans_x
