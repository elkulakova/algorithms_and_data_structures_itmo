import random
import numpy as np

def generate_data(p=None):
    if not p:
        p = random.randint(1, 10)
        n = 2 ** p
    else:
        n = 2 ** p
    matrix_a = [f'{" ".join(map(str, [random.randint(-10**4, 10**4) for _ in range(n)]))}\n' for _ in range(n)]
    matrix_b = [f'{" ".join(map(str, [random.randint(-10**4, 10**4) for _ in range(n)]))}\n' for _ in range(n)]
    all_data = [f'{n}\n', f'{" ".join(map(str, matrix_a))}', f'{" ".join(map(str, matrix_b))}']

    with open('input.txt', 'w') as f:
        f.writelines(all_data)