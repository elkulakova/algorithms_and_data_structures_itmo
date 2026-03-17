from effective_fibs import *
from measurments import *

@measure_memory_usage
@timeit
def last_fib_digit():
    with open('input.txt') as f:
        n = int(f.readline())

    if n >= 0:
        equiv_fib = n % 60
        if equiv_fib <= 1:
            val = equiv_fib
        else:
            val = effect_fibs(equiv_fib) % 10

        with open('output.txt', 'w') as f:
            f.write(str(val))
        return val
    return 'input value cannot be negative!'

if __name__ == "__main__":
    for i in (0, 331, 327305, 10000000):
        with open('input.txt', 'w') as fl:
            fl.write(str(i))
        print(f'FIBONACCI LAST DIGIT {last_fib_digit()}\n\n')
