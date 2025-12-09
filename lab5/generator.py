import random
import numpy as np

def heap_generator(n=None):
    if n is None:
        n = random.randint(1, 10**6)
    arr = random.choices(range(1, 10**6), k=n)

    with open('input.txt', 'w') as f:
        f.writelines([f'{n}\n', f'{" ".join(map(str, arr))}\n'])
    return None


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

def packages_generator(n=None, s=None):
    if n is None:
        n = random.randint(1, 10**5)
    if s is None:
        s = random.randint(1, 10**5)

    at = sorted(random.choices(range(0, 10**6 + 1), k=n))
    pt = random.choices(range(0, 10**3 + 1), k=n)

    with open('input.txt', 'w') as f:
        f.write(f'{s} {n}')
        for a, p in zip(at, pt):
            f.write(f'\n{a} {p}')
    return None

def flows_generator(n=None, m=None):
    if n is None:
        n = random.randint(1, 10**5)
    if m is None:
        m = random.randint(1, 10**5)

    times = random.choices(range(0, 10**9 + 1), k=m)

    with open('input.txt', 'w') as f:
        f.write(f'{n} {m}\n')
        f.write(" ".join(map(str, times)))