import random
import numpy as np

def abracadabra(n=None):
    if not n:
        n = random.randint(1, 10**5)
    let_nums = np.random.randint(ord('A'), ord('Z'), size=n)
    string = ''
    for num in let_nums:
        string += chr(num)

    with open('input.txt', 'w') as f:
        f.writelines([f'{str(n)}\n', string])

    return None
