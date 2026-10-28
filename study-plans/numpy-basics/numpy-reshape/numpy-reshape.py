import numpy as np

def reshape_array(data: list, operation: str) -> np.ndarray:
    """
    Returns a float64 array with the shape selected by operation.
    """
    data = np.asarray(data, dtype= np.float64)
    if operation == 'transpose':
        return data.T
    elif operation == "flatten":
        return data.flatten()
    else:
        return data.reshape(1, data.shape[0], data.shape[1])
    