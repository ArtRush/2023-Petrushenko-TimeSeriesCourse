import numpy as np
import pandas as pd
import math

import stumpy
from stumpy import config


def compute_mp(ts1, m, exclusion_zone=None, ts2=None):
    """
    Compute the matrix profile.

    Parameters
    ----------
    ts1 : numpy.ndarrray
        The first time series.

    m : int
        The subsequence length.

    exclusion_zone : int, default = None
        Exclusion zone.

    ts2 : numpy.ndarrray, default = None
        The second time series.

    Returns
    -------
    output : dict
        The matrix profile structure 
        (matrix profile, matrix profile index, subsequence length, 
        exclusion zone, the first and second time series).
    """

    config.STUMPY_EXCL_ZONE_DENOM = exclusion_zone

    mp = stumpy.stump(ts1, m=m, T_B=ts2)

    return {'mp': mp[:, 0],
            'mpi': mp[:, 1],
            'm' : m,
            'excl_zone': exclusion_zone,
            'data': {'ts1' : ts1, 'ts2' : ts2}
            }