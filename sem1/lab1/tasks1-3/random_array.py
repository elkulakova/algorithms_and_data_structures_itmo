import random
import numpy as np

def generate_array(n=None):
    if not n:
        n = random.randint(1, 10**3)
    arr = np.random.randint(-10**9, 10**9, size=n)

    with open('input.txt', 'w') as f:
        f.writelines([f'{str(n)}\n', ", ".join(map(str, arr))])

    return None