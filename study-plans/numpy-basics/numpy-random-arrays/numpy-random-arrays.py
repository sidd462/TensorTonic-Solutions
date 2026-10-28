import numpy as np

def generate_random_array(shape: list, kind: str, seed: int) -> np.ndarray:
    """
    Returns a seeded 2D float64 random array with the requested shape.
    """
    rng = np.random.default_rng(seed = seed)

    return rng.normal(0, 1, tuple(shape)) if kind == "normal" else rng.random(shape[0]*shape[1]).reshape(tuple(shape))
