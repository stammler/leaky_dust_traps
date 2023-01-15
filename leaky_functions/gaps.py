import numpy as np


def Kanagawa2017_gap_profile(r, a, q, h, alpha0):
    """Function calculates the gap profile according Kanagawa et al. (2017).

    Parameters
    ----------
    r : array
        Radial grid
    a : float
        Semi-majo axis of planet
    q : float
        Planet-star mass ratio
    h : float
        Aspect ratio at planet location
    alpha0 : float
        Unperturbed alpha viscosity parameter

    Returns
    -------
    f : array
        Pertubation of surface density due to planet"""

    # Unperturbed return value
    ret = np.ones_like(r)

    # Distance to planet (normalized)
    dist = np.abs(r-a)/a

    qp = q + 1.e-100

    K = qp**2 / (h**5 * alpha0)  # K
    Kp = qp**2 / (h**3 * alpha0)  # K prime
    Kp4 = Kp**(0.25)  # Fourth root of K prime
    SigMin = 1. / (1 + 0.04*K)  # Sigma minimum
    SigGap = 4 / Kp4 * dist - 0.32  # Sigma gap
    dr1 = (0.25*SigMin + 0.08) * Kp**0.25  # Delta r1
    dr2 = 0.33 * Kp**0.25  # Delta r2

    # Gap edges
    mask1 = np.logical_and(dr1 < dist, dist < dr2)
    ret = np.where(mask1, SigGap, ret)
    # Gap center
    mask2 = dist < dr1
    ret = np.where(mask2, SigMin, ret)

    return ret
