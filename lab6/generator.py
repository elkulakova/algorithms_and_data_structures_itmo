import random
import numpy as np
from faker import Faker


def set_generator(n=None):
    if n is None:
        n = random.randint(1, 5 * 10**5)

    opers = ['A', 'D', '?']
    operations_list = []
    for _ in range(n):
        o = random.choice(opers)
        x = random.randint(-10**18, 10**18)
        operations_list.append(f'{o} {x}')

    with open('input.txt', 'w') as f:
        f.write(f'{n}\n')
        f.write('\n'.join(operations_list))

    return None

def reqs_generator(n=None):
    fake = Faker('en_US')
    if n is None:
        n = random.randint(1, 10**5)
    words = ['add', 'del', 'find']
    with open('input.txt', 'w') as f:
        f.write(f'{n}')
        for _ in range(n):
            word = random.choice(words)
            k = random.randint(1, 7)
            num1 = random.randint(1, 9)
            if k == 1:
                number = f'{num1}'
            else:
                num2 = random.choices(range(0, 9), k=k-1)
                number = f'{num1}{"".join(map(str, num2))}'
            if word == 'add':
                name = fake.name()
                while len(name) > 15:
                    name = fake.name()
                f.write(f'\n{word} {number} {name}')
            else:
                f.write(f'\n{word} {number}')
    return None

def array_flow(n=None):
    alpha_range = list(range(ord('A'), ord('Z'))) + list(range(ord('a'), ord('z')))
    if n is None:
        n = random.randint(1, 5 * 10**5)
    words = ['put', 'delete', 'get', 'prev', 'next']
    with open('input.txt', 'w') as f:
        f.write(f'{n}')
        for _ in range(n):
            word = random.choice(words)
            k = random.randint(1, 20)
            m = random.randint(1, 20)
            x = random.choices(alpha_range, k=k)
            x_str = ''.join(map(chr, x))
            if word == 'put':
                y = random.choices(alpha_range, k=m)
                y_str = ''.join(map(chr, y))
                f.write(f'\n{word} {x_str} {y_str}')
            else:
                f.write(f'\n{word} {x_str}')
    return None

def elections_generator(n=None, k=None):
    fake = Faker('en_US')
    if n is None:
        n = random.randint(1, 50)
    if k is None:
        k = random.randint(1, 20)

    surnames_list = []
    for _ in range(k):
        surname = fake.last_name()
        while surname in surnames_list:
            surname = fake.last_name()
        surnames_list.append(surname)

    with open('input.txt', 'w') as f:
        for _ in range(n):
            surname = random.choice(surnames_list)
            votes = random.randint(1, 6 * 10**6)
            f.write(f'{surname} {votes}\n')
    return None

def gems_generator(n=None, k=None):
    alpha_range = list(range(ord('a'), ord('z')))
    if n is None:
        n = random.randint(1, 10**5)
    if k is None:
        k = random.randint(1, 676)

    with open('input.txt', 'w') as f:
        f.write(f'{n} {k}')
        gems_str = "".join(map(chr, random.choices(alpha_range, k=n)))
        f.write(f'\n{gems_str}')
        for _ in range(k):
            pair = "".join(map(chr, random.choices(alpha_range, k=2)))
            f.write(f'\n{pair}')
    return None

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