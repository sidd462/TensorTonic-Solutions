import numpy as np
import math
def vector_norms(v: list) -> np.ndarray:
    """
    Returns a float64 array containing the L1, L2, and infinity norms.
    """
    return np.asarray([
        sum([abs(v[i]) for i in range(len(v))]),
        math.sqrt(sum([v[i] ** 2 for i in range(len(v))])),
        max([abs(v[i]) for i in range(len(v))])
                      ])