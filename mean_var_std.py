import numpy as np

def calculate(values):
    if len(values) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(values).reshape(3, 3)

    operations = {
        "mean": np.mean,
        "variance": np.var,
        "standard deviation": np.std,
        "max": np.max,
        "min": np.min,
        "sum": np.sum,
    }

    result = {}

    for name, func in operations.items():
        result[name] = [
            func(matrix, axis=0).tolist(),
            func(matrix, axis=1).tolist(),
            func(matrix)
        ]

    return result
