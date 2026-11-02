import numpy as np
import math
def dot(A, B):
    return float(sum([A[i] * B[i] for i in range(len(A))]))
def mag(A):
    return float(math.sqrt(sum([A[i]**2 for i in range(len(A))])))
def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a float.
    """
    if mag(a) == 0 or mag(b) ==0:
        return float(0)
    return dot(a, b)/(mag(a) * mag(b))