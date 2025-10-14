import random
import numpy as np

def generate_array(n=None):
    if n not in range(0, 10**3 + 1):
        n = random.randint(0, 10**3)
    arr = np.random.randint(-10**3, 10**3, size=n)
    v = np.random.randint(-10**3, 10**3)

    with open('input.txt', 'w') as f:
        f.writelines([f'{" ".join(map(str, arr))}\n', str(v)])

    return None