import numpy as np
import math
def pe_even(a, b, base, d_model):
    return math.sin(a/(base**(b/d_model)))
def pe_odd(a, b, base, d_model):
    return math.cos(a/(base**(b/d_model)))

def positional_encoding(seq_len: int, d_model: int, base: float = 10000.0) -> np.ndarray:
    """
    Returns a NumPy array of shape (seq_len, d_model).
    """
    pe = []
    for i in range(seq_len):
        temp_r = []
        for j in range(d_model):
            if j % 2 == 0:
                temp_r.append(pe_even(i, j, base, d_model))
            else:
                temp_r.append(pe_odd(i, j - 1, base, d_model))
        temp_r = np.asarray(temp_r)
        pe.append(temp_r)
    return np.asarray(pe)