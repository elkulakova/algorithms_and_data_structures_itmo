import random
import numpy as np

def tree_generator(n=None):
    if n is None:
        n = random.randint(1, 10**5)
    tree = random.choices(range(0, n), k=n)
    root_index = random.randint(0, n-1)
    tree[root_index] = -1

    with open('input.txt', 'w') as f:
        f.write(f'{n}\n')
        f.write(" ".join(map(str, tree)))

    return None