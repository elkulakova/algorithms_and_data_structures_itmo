def effect_fibs():
    with open('input_extra.txt') as f:
        n = int(f.readline())

    n_bit_len = n.bit_length()
    cur_pos = 0
    cur_val, next_val = (cur_pos, cur_pos+1)
    for i in range(n_bit_len):
        cur_pos *= 2
        cur_val, next_val = (cur_val*(2*next_val - cur_val), cur_val**2 + next_val**2)

        if (n >> n_bit_len - 1 - i) & 1:
            cur_pos += 1
            cur_val, next_val = (next_val, cur_val+next_val)

    with open('output_extra.txt', 'w') as f:
        f.write(str(cur_val))

    return cur_val
