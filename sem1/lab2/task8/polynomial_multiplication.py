from polynome import *
from measurments import *

def get_data():
    with open('input.txt') as f:
        data = f.readlines()
    n, pad = int(data[0]), int(data[1])
    a, b = list(map(int, data[2].split())), list(map(int, data[3].split()))
    return n, pad, a, b

@measure_performance
def poly_mult_4(p, a, b):
    if p == 1:
        return [a[0] * b[0]]
    if p > 2:
        a1 = a[:p//2]
        a2 = a[p//2:]
        b1 = b[:p // 2]
        b2 = b[p // 2:]

        c1 = poly_mult_4(p//2, a1, b1)
        c2 = poly_mult_4(p // 2, a2, b1)
        c3 = poly_mult_4(p // 2, a1, b2)
        c4 = poly_mult_4(p // 2, a2, b2)

        mid_sum = [x+y for x,y in zip(c2, c3)]

        fp = c1[:p//2]
        mp1 = [x+y for x, y in zip(c1[p//2:], mid_sum[:(p//2)-1])]
        me = [mid_sum[(p//2)-1]]
        mp2 = [x+y for x, y in zip(mid_sum[(p//2):], c4[:(p//2)-1])]
        lp = c4[(p//2)-1:]
        fin_arr = fp + mp1 + me + mp2 + lp
        return fin_arr
    return [a[0]*b[0], a[1]*b[0]+a[0]*b[1], a[1]*b[1]]

@measure_performance
def poly_mult_3(p, a, b):
    if p == 1:
        return [a[0] * b[0]]
    if p > 2:
        a1 = a[:p//2]
        a2 = a[p//2:]
        b1 = b[:p // 2]
        b2 = b[p // 2:]

        temp1 = [x + y for x, y in zip(a1, a2)]
        temp2 = [x + y for x, y in zip(b1, b2)]
        c1 = poly_mult_3(p//2, a1, b1)
        c2 = poly_mult_3(p // 2, temp1, temp2)
        c3 = poly_mult_3(p // 2, a2, b2)
        c4 = [x - y - z for x, y, z in zip(c2, c1, c3)] #a1b2 + a2b1

        fp = c1[:p//2]
        mp1 = [x+y for x, y in zip(c1[p//2:], c4[:(p//2)-1])]
        me = [c4[(p//2)-1]]
        mp2 = [x+y for x, y in zip(c4[(p//2):], c3[:(p//2)-1])]
        lp = c3[(p//2)-1:]
        fin_arr = fp + mp1 + me + mp2 + lp
        return fin_arr
    return [a[0]*b[0], a[1]*b[0]+a[0]*b[1], a[1]*b[1]]

if __name__ == "__main__":
    generate_coefs()
    real_len, pad_len, coef_a, coef_b = get_data()
    zrs = (pad_len - real_len) * 2
    #mult_coefs4 = poly_mult_4(pad_len, coef_a, coef_b)[zrs:]
    mult_coefs3 = poly_mult_3(pad_len, coef_a, coef_b)[zrs:]
    #assert all([mult_coefs4[i] == mult_coefs3[i] for i in range(real_len)]), 'not equal.....'
    with open('output.txt', 'w') as fl:
        fl.write(" ".join(map(str, mult_coefs3)))
    print(mult_coefs3)
