import numpy as np
import random
from merging_norm import *

def generate_arrays(n=None, k=None):
    if not n:
        n = random.randint(1, 10**5)
    if not k:
        k = random.randint(1, 10**5)
    arr_a = random.sample(range(1, 10**9), n)
    print('created a')
    arr_b = np.random.randint(1, 10**9 + 1, k)
    print('created b')
    fin_data = [f'{str(n)}\n', f'{" ".join(map(str, arr_a))}\n', f'{str(k)}\n', f'{" ".join(map(str, arr_b))}']

    with open('input.txt', 'w') as f:
        f.writelines(fin_data)
    return None