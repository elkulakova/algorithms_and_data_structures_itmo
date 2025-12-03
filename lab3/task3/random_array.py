import random


def generate_array(n=None, k=None):
    if not n:
        n = random.randint(1, 10 ** 5)
    if not k:
        k = random.randint(1, 10 ** 5)
    fin_arr = random.choices(range(-10 ** 9, 10 ** 9), k=n)

    with open('input.txt', 'w') as f:
        f.writelines([f'{str(n)} {str(k)}\n', " ".join(map(str, fin_arr))])

    return None
