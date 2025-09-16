from measurments import *

@measure_memory_usage
@timeit
def effect_fibs():
    with open('input.txt') as f:
        n = int(f.readline())

    if 0 <= n <= 20577:
        n_bit_len = n.bit_length()
        cur_pos = 0
        cur_val, next_val = (0, 1)
        for i in range(n_bit_len):
            cur_pos *= 2
            cur_val, next_val = (cur_val*(2*next_val - cur_val), cur_val**2 + next_val**2)

            if (n >> n_bit_len - 1 - i) & 1:
                cur_pos += 1
                cur_val, next_val = (next_val, cur_val+next_val)

        with open('output.txt', 'w') as f:
            f.write(str(cur_val))

        return cur_val
    return 'input value cannot be out of range 0 - 20577!'

if __name__ == "__main__":
    for i in (0, 10, 45):
        with open('input.txt', 'w') as fl:
            fl.write(str(i))
        print(f'FIBONACCI VALUE {effect_fibs()}\n\n')