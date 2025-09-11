from effective_fibs import *

def last_fib_digit():
    with open('input.txt') as f:
        n = int(f.readline())

    if n <= 1:
        with open('output.txt', 'w') as f:
            f.write(str(n))
        return n
    equiv_fib = n % 60

    with open('input_extra.txt', 'w') as f:
        f.write(str(equiv_fib))

    val = effect_fibs() % 10

    with open('output.txt', 'w') as f:
        f.write(str(val))
    return val

print(last_fib_digit())