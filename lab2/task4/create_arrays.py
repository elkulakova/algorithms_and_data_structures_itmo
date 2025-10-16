import numpy as np
import random
from lab2.task1_2.merging_norm import *

def generate_arrays(n=None, k=None):
    if not n:
        n = random.randint(1, 10**5)
    if not k:
        k = random.randint(1, 10**5)
    arr_a = merge_sort(n, np.random.randint(1, 10**9 + 1, n))
    arr_b = merge_sort(k, np.random.randint(1, 10**9 + 1, k))
    fin_data = [f'{str(n)}\n', f'{" ".join(map(str, arr_a))}\n', f'{str(k)}\n', f'{" ".join(map(str, arr_b))}']

    with open('input.txt', 'w') as f:
        f.writelines(fin_data)

    return None