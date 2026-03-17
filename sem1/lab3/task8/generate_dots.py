import random

def generate_dots(n=None, k=None):
    if not n:
        n = random.randint(1, 100000)
    if not k:
        k = random.randint(1, 100000)

    dots = [(random.randint(-10**9, 10**9), random.randint(-10**9, 10**9))  for _ in range(n)]

    with open('input.txt', 'w') as f:
        f.write(f"{n} {k}\n")
        for dot in dots:
            f.write(f"{dot[0]} {dot[1]}\n")

    return None