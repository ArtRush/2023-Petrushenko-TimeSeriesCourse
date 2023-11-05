import numpy as np

import stumpy

from modules.utils import *


def top_k_motifs(matrix_profile, top_k=3):
    """
    Find the top-k motifs based on matrix profile.

    Parameters
    ---------
    matrix_profile : dict
        The matrix profile structure.

    top_k : int
        Number of motifs.

    Returns
    --------
    motifs : dict
        Top-k motifs (left and right indices and distances).
    """

    motifs_dist, motifs_idx = stumpy.motifs(T=matrix_profile['data']['ts1'], P=matrix_profile['mp'], max_motifs=top_k)

    return {
        "indices" : motifs_idx,
        "distances" : motifs_dist
        }
