import random
import numpy as np


def generate_array(n=None, pattern=None):
    if not n:
        n = random.randint(1, 10 ** 4)
    if pattern == 'asc':
        fin_arr = sorted(np.random.randint(-10 ** 9, 10 ** 9, size=n))
    elif pattern == 'desc':
        fin_arr = sorted(np.random.randint(10 ** 9, 10 ** 10, size=n), reverse=True)
    elif pattern == 'dups':
        fin_arr = random.choices(range(-10 ** 9, 10 ** 9), k=n)
    elif pattern == 'dups&asc':
        fin_arr = sorted(random.choices(range(-10 ** 9, 10 ** 9), k=n))
    elif pattern == 'dups&desc':
        fin_arr = sorted(random.choices(range(10 ** 9, 10 ** 10), k=n), reverse=True)
    else:
        fin_arr = np.random.randint(-10 ** 9, 10 ** 9, size=n)

    with open('input.txt', 'w') as f:
        f.writelines([f'{str(n)}\n', " ".join(map(str, fin_arr))])

    return None
