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

def expression_generator(n=None):
    if n is None:
        n = random.randint(0, 14)

    if n > 0:
        digits = np.random.randint(0,10, size=n)
        operations = np.random.choice(['+', '-', '*'], size=n-1)

        expr = "".join(map(str, [digits[i // 2] if i % 2 == 0 else operations[i // 2] for i in range(2*n - 1)]))
        return expr, 2*n + 1
    else:
        return np.random.randint(0, 10, 1), 0

def cards_generator(n=None, m=None):
    if n is None:
        n = random.randint(1, 35)
    if m is None:
        if 36 - n > 4:
            m = random.randint(1, 4)
        else:
            m = random.randint(1, 36 - n)

    rang = ['6','7','8','9','T','J','Q','K','A']
    suit = ['C','D','H','S']

    trump = random.choice(suit)
    player = []
    table = []
    for i in range(n):
        new = False
        while not new:
            r = random.choice(rang)
            s = random.choice(suit)
            card = r + s
            if card not in player:
                player.append(card)
                new = True

    for i in range(m):
        new = False
        while not new:
            r = random.choice(rang)
            s = random.choice(suit)
            card = r + s
            if card not in player and card not in table:
                table.append(card)
                new = True

    return n, " ".join(map(str, player)), m, " ".join(map(str, table)), trump

def square_generator(n=None, m=None):
    if n is None:
        n = random.randint(1, 30)
    if m is None:
        m = random.randint(1, 30)
        while m*n > 30:
            m = random.randint(1, 30)

    return n, m

def routes_generator(n=None):
    if n is None:
        n = random.randint(1, 13)
    arr = [[10**6 + 1] * n for _ in range(n)]

    for i in range(n):
        arr[i][i] = 0

    for i in range(n):
        for j in range(i + 1, n):
            dist = random.randint(1, 10 ** 6)
            arr[i][j] = arr[j][i] = dist

    return n, arr