import random
import string

def generate_string(length=None):
    chars = string.ascii_letters + string.digits + string.punctuation
    brackets = '()[]{}'

    if length is None:
        length = random.randint(1, 10 ** 5)

    str_list = [random.choice(chars) for _ in range(length)]

    if length > 1:
        num_brackets = random.randint(1, length // 2)
    else:
        num_brackets = 1

    positions = random.sample(range(length), num_brackets)

    for pos in positions:
        str_list[pos] = random.choice(brackets)

    result = ''.join(str_list)

    with open('input.txt', 'w') as f:
        f.write(result)

    return None