import numpy as np


def matrix_stats(matrix: np.ndarray) -> dict:
    if matrix.ndim != 2:
        raise ValueError
    result = dict()
    summation = matrix.sum()
    rows = matrix.sum(1)
    columns = matrix.sum(0)
    result.update({'total_sum': summation, 'row_sums': rows, 'column_sums': columns})
    return result


print(matrix_stats(np.arange(3 * 4).reshape(3, 4)))
