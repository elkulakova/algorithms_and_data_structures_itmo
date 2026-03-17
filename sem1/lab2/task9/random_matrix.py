import random
import numpy as np
import math

def generate_data(n=None):
    if not n:
        n = random.randint(1, 3)

    if not np.log2(n).is_integer():
        k = math.ceil(np.log2(n))
        p = 2 ** k
        a = [[random.randint(-10**4, 10**4) for _ in range(n)] for _ in range(n)]
        b = [[random.randint(-10**4, 10**4) for _ in range(n)] for _ in range(n)]
        padw = (p-n)
        a_fin = np.pad(a, ((0, padw), (0, padw)), 'constant')
        b_fin = np.pad(b, ((0, padw), (0, padw)), 'constant')
        matrix_a = [f'{" ".join(map(str, row))}\n' for row in a_fin]
        matrix_b = [f'{" ".join(map(str, row))}\n' for row in b_fin]
    else:
        matrix_a = [f'{" ".join(map(str, [random.randint(-10**4, 10**4) for _ in range(n)]))}\n' for _ in range(n)]
        matrix_b = [f'{" ".join(map(str, [random.randint(-10**4, 10**4) for _ in range(n)]))}\n' for _ in range(n)]
        p = n
    all_data = [f'{n}\n', f'{p}\n', f'{" ".join(map(str, matrix_a))}', f'{" ".join(map(str, matrix_b))}']

    with open('input.txt', 'w') as f:
        f.writelines(all_data)