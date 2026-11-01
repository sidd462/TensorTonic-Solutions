import numpy as np
import math
def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a float.
    """
    return math.sqrt(sum([(x[i] - y[i]) ** 2 for i in range(len(x))]))