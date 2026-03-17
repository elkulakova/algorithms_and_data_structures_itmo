import random
import numpy as np

def cash_generator(s=None, n=None):
    if s is None:
        s = random.randint(1, 1000)
    if n is None:
        n = random.randint(1, 100)

    limits = random.choices(list(range(1, 101)), k=n)
    cash = sorted(np.random.randint(1, 1001, n))
    with open('input.txt', 'w') as f:
        f.write(f'{s} {n}\n')
        f.write(f'{' '.join(map(str, cash))}\n')
        f.write(f'{" ".join(map(str, limits))}')

import string

def generate_template_and_string(t=None, s=None):
    if t is None:
        t = random.randint(0, 10000)
    if s is None:
        s = random.randint(0, 10000)

    letters = string.ascii_lowercase + '.'
    specials = ['?', '*']

    template = []
    for _ in range(t):
        if random.random() < 0.15:
            template.append(random.choice(specials))
        else:
            template.append(random.choice(letters))
    template = ''.join(template)

    string_chars = [random.choice(letters) for _ in range(s)]
    string_s = ''.join(string_chars)

    with open('input.txt', 'w') as f:
        f.write(f'{template}\n{string_s}')

def levenshtein_generator(n=None, m=None):
    if m is None:
        m = random.randint(1, 5000)
    if n is None:
        n = random.randint(1, 5000)

    letters = string.ascii_lowercase

    init = ''.join(random.choice(letters) for _ in range(n))
    res = ''.join(random.choice(letters) for _ in range(m))

    with open('input.txt', 'w') as f:
        f.write(f'{init}\n{res}')

def array_generator(n=None, m=None):
    if m is None:
        m = random.randint(1, 100)
    if n is None:
        n = random.randint(1, 100)

    arra = [random.randint(-10**9 + 1, 10**9) for _ in range(n)]
    arrb = [random.randint(-10**9 + 1, 10**9) for _ in range(m)]

    with open('input.txt', 'w') as f:
        f.write(f'{n}\n{" ".join(map(str, arra))}\n{m}\n{" ".join(map(str, arrb))}')