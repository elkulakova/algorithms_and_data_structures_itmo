import random


def generate_array(n=None, pattern=None):
    if not n:
        n = random.randint(1, 5000)
    if pattern == 'asc':
        fin_arr = sorted(random.choices(range(0, 1000), k=n))
    elif pattern == 'desc':
        fin_arr = sorted(random.choices(range(0, 1000), k=n), reverse=True)
    else:
        fin_arr = random.choices(range(0, 1000), k=n)

    with open('input.txt', 'w') as f:
        f.writelines([f'{str(n)}\n', " ".join(map(str, fin_arr))])

    return None