import numpy as np
from functions.probabilities_f import bouncing_pstick


def bouncing(s):
    """Function returns the stcking probabilies including the sticking-bouncing transition of Windmark et al. (2012).

    Parameters
    ----------
    s : DustPy Simulation object

    Returns
    -------
    p_stick : array
        Sticking probabilities."""
    return bouncing_pstick(
        s.dust.v.rel.tot,
        s.grid.m,
    )
