from measurments import *

def effect_fibs(position):
    if position >= 0:
        n_bit_len = position.bit_length()
        cur_pos = 0
        cur_val, next_val = (0, 1)
        for i in range(n_bit_len):
            cur_pos *= 2
            cur_val, next_val = (cur_val * (2 * next_val - cur_val), cur_val ** 2 + next_val ** 2)

            if (position >> n_bit_len - 1 - i) & 1:
                cur_pos += 1
                cur_val, next_val = (next_val, cur_val + next_val)

        return cur_val
    return 'input value cannot be negative!'


if __name__ == "__main__":
    effect_fibs()