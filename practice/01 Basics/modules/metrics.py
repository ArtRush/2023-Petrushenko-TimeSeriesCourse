import numpy as np


def ED_distance(ts1: np.ndarray, ts2: np.ndarray):
    """
    Calculate the Euclidean distance.

    Parameters
    ----------
    ts1 : numpy.ndarray
        The first time series.

    ts2 : numpy.ndarray
        The second time series.

    Returns
    -------
    ed_dist : float
        Euclidean distance between ts1 and ts2.
    """
    
    sum = 0
    for ts1_point, ts2_point in zip(ts1, ts2):
        sum += (ts2_point - ts1_point) * (ts2_point - ts1_point)
    ed_dist = sum ** (1/2)
    
    return ed_dist


def norm_ED_distance(ts1, ts2):
    """
    Calculate the normalized Euclidean distance.

    Parameters
    ----------
    ts1 : numpy.ndarray
        The first time series.

    ts2 : numpy.ndarray
        The second time series.

    Returns
    -------
    norm_ed_dist : float
        The normalized Euclidean distance between ts1 and ts2.
    """

    norm_ed_dist = 0

    # INSERT YOUR CODE 

    return norm_ed_dist


def DTW_distance(ts1: np.ndarray, ts2: np.ndarray, r=None):
    """
    Calculate DTW distance.

    Parameters
    ----------
    ts1 : numpy.ndarray
        The first time series.

    ts2 : numpy.ndarray
        The second time series.

    r : float
        Warping window size.
    
    Returns
    -------
    dtw_dist : float
        DTW distance between ts1 and ts2.
    """

    n, m = len(ts1), len(ts2)
    dtw_dist = np.zeros((n + 1, m + 1))

    for i in range(n + 1):
        for j in range(m + 1):
            dtw_dist[i, j] = np.inf
    dtw_dist[0, 0] = 0

    for index in range(1, n + 1):
        for jndex in range(1, m + 1):
            cost = (ts2[index - 1] - ts1[jndex  - 1]) * (ts2[index - 1] - ts1[jndex - 1])
            # Take last min from a square box
            last_min = np.min([
                dtw_dist[index - 1, jndex],
                dtw_dist[index, jndex - 1],
                dtw_dist[index - 1, jndex - 1]
                ])
            dtw_dist[index, jndex] = cost + last_min
    return dtw_dist[n, m]