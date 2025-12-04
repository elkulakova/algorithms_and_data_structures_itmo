import random
import numpy as np


def generate_array(n=None, k=None):
    if not n:
        n = random.randint(1, 10 ** 5)
    if not k:
        k = random.randint(1, n)
    fin_arr = np.random.randint(0, 10 ** 5, size=n)

    with open('input.txt', 'w') as f:
        f.writelines([f'{str(n)}\n', f'{" ".join(map(str, fin_arr))}\n', f'{str(k)}'])

    return None
