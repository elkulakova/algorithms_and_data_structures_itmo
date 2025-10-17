import random
import numpy as np
import math

def generate_coefs(n=None):
    if not n:
        n = random.randint(1, 25)

    if not np.log2(n).is_integer():
        k = math.ceil(np.log2(n))
        p = 2 ** k
        a = [0 for _ in range(p-n)] + [random.randint(-10**4, 10**4) for _ in range(n)]
        b = [0 for _ in range(p - n)] + [random.randint(-10 ** 4, 10 ** 4) for _ in range(n)]
    else:
        a = [random.randint(-10 ** 4, 10 ** 4) for _ in range(n)]
        b = [random.randint(-10 ** 4, 10 ** 4) for _ in range(n)]
        p = n
    all_data = [f'{n}\n', f'{p}\n', f'{" ".join(map(str, a))}\n', f'{" ".join(map(str, b))}']

    with open('input.txt', 'w') as f:
        f.writelines(all_data)