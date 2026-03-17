import random
import numpy as np


def stations_generator(d=None, m=None, n=None):
    if d is None:
        d = random.randint(1, 10**5)
    if m is None:
        m = random.randint(1, 400)
    if n is None:
        n = random.randint(1, 300)

    arr = np.sort(np.random.choice(np.arange(1, d), size=n, replace=False)) if d != 1 else np.array(1)
    return d, m, n, arr

def segments_generator(n=None):
    if n is None:
        n = random.randint(1, 100)

    arr = []
    for i in range(n):
        a = random.randint(1, 10**9)
        b = random.randint(a + 1, 10**9)
        arr.append((a, b))

    return n, arr

def sequences_generator(n=None):
    if n is None:
        n = random.randint(1, 4000)
    arr = []
    for i in range(1, n+1):
        arr.append(random.randint(1, i))

    return n, arr