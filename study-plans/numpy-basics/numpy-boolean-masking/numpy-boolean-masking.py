import numpy as np
import copy
def row_summary(data: list, threshold: float) -> np.ndarray:
    """
    Returns a float64 array of shape (3, m, n): mask, any-row, all-row.
    """
    data = np.asarray(data, dtype = np.float64)
    Element_mask = copy.deepcopy(data)
    Element_mask = (Element_mask > threshold).astype(np.float64)

    any = copy.deepcopy(data)
    for i in range(any.shape[0]):
        if np.any(Element_mask[i]):
            continue
        else:
            any[i] = np.zeros(any[i].shape)
    any = any.astype(np.float64)
    all = copy.deepcopy(data)
    for i in range(all.shape[0]):
        if np.all(Element_mask[i]):
            continue
        else:
            all[i] = np.zeros(all[i].shape)
    all = all.astype(np.float64)
    return np.stack([Element_mask, any, all])
    
    
    
    
