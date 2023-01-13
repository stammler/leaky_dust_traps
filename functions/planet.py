import dustpy.constants as c
import numpy as np


def Mp_slow(s):
    """This function returns a time dependent planetary mass with slow growth.

    The planet reaches
    20 Earth masses after 1 Myrs
    50 Earth masses after 4 Myrs
    1 Jupiter mass after 10 Myrs

    Parameters
    ----------
    s : DustPy simulation object

    Returns
    Mp : float
        Planetary mass"""

    M = np.array([
        0.,
        20.,
        50.,
        c.M_jup / c.M_earth
    ]) * c.M_earth

    t = np.array([
        0.,
        1.,
        4.,
        10.
    ]) * 1.e6 * c.year

    for i in range(1, len(M)):
        if s.t <= t[i]:
            return (M[i] - M[i-1]) / (t[i] - t[i-1]) * (s.t - t[i-1]) + M[i-1]

    return M[-1]


def Mp_fast(s):
    """This function returns a time dependent planetary mass with fast growth.

    The planet reaches
    40 Earth masses after 1 Myrs
    50 Earth masses after 4 Myrs
    1 Jupiter mass after 10 Myrs

    Parameters
    ----------
    s : DustPy simulation object

    Returns
    Mp : float
        Planetary mass"""

    M = np.array([
        0.,
        40.,
        50.,
        c.M_jup / c.M_earth
    ]) * c.M_earth

    t = np.array([
        0.,
        1.,
        4.,
        10.
    ]) * 1.e6 * c.year

    for i in range(1, len(M)):
        if s.t <= t[i]:
            return (M[i] - M[i-1]) / (t[i] - t[i-1]) * (s.t - t[i-1]) + M[i-1]

    return M[-1]
