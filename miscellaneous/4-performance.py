import math
import random
import numpy as np


# 표준편차 계산
def standard_deviation(lst):
    m = sum(lst) / len(lst)
    variance = sum([(value - m) ** 2 for value in lst])
    return math.sqrt(variance / len(lst))


rands = [random.random() for _ in range(0, 1000000)]
numpy_rands = np.array(rands)

# %timeit -n 100 np.std(numpy_rands)
# 3.28 ms ± 214 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)
# %timeit -n 100 standard_deviation(rands)
# 131 ms ± 1.03 ms per loop (mean ± std. dev. of 7 runs, 100 loops each)
