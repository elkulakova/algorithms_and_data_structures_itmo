import random

def generate_dots(num_dots=None, k=None):
    if not num_dots:
        n = random.randint(1, 100000)
    if not k:
        k = random.randint(1, 100000)
    n = num_dots

    dots = [(random.randint(-10**9, 10**9), random.randint(-10**9, 10**9))  for _ in range(n)]

    with open('input.txt', 'w') as f:
        f.write(f"{n} {k}\n")
        for dot in dots:
            f.write(f"{dot[0]} {dot[1]}\n")

    return None