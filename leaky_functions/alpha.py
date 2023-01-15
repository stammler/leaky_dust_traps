from leaky_functions.gaps import Kanagawa2017_gap_profile
import numpy as np
from scipy.interpolate import interp1d


def alpha(s):
    """Function returns the alpha viscosity profile to create planetary gaps in the gas surface density.

    Parameters
    ----------
    s : DustPy simulation object

    Returns
    -------
    alpha : array
        alpha viscosity profile"""

    # Unperturbed profile
    alpha0 = s.ini.gas.alpha
    alpha = alpha0 * np.ones_like(s.gas.alpha)

    # Iterate over all planets and add viscosity pertubation
    for name, p in s.planets.__dict__.items():
        # Skip hidden fields
        if name[0] == "_":
            continue

        # Dimensionless planet mass
        q = p.M / s.star.M

        # Aspect ratio
        h = s.gas.Hp / s.grid.r
        # Interpolate aspect ratio on planet location
        f_h = interp1d(s.grid.r, h)
        hp = f_h(p.a)

        # Inverse alpha profile
        alpha /= Kanagawa2017_gap_profile(s.grid.r, p.a, q, hp, alpha0)

    return alpha
