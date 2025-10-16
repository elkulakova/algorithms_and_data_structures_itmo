from random_matrix import *
import numpy as np
from measurments import *

def get_data():
    with open('input.txt') as f:
        data = f.readlines()
    n = int(data[0])
    mat_a, mat_b = np.array([list(map(int, i.split())) for i in data[1:n+1]]), np.array([list(map(int, i.split())) for i in data[n+1:]])
    return n, mat_a, mat_b

@measure_performance
def shtrassen_multiplication(n, x, y):
    if n >= 2:
        q = n // 2

        a = np.array([i[:q] for i in x[:q]])
        b = np.array([i[q:] for i in x[:q]])
        c = np.array([i[:q] for i in x[q:]])
        d = np.array([i[q:] for i in x[q:]])

        e = np.array([i[:q] for i in y[:q]])
        f = np.array([i[q:] for i in y[:q]])
        g = np.array([i[:q] for i in y[q:]])
        h = np.array([i[q:] for i in y[q:]])

        # p1 = a * (f - h)
        # p2 = (a + b) * h
        # p3 = (c + d) * e
        # p4 = d * (g - e)
        # p5 = (a + d) * (e + h)
        # p6 = (b - d) * (g + h)
        # p7 = (a - c) * (e + f)

        p1 = shtrassen_multiplication(len(a), a, matrix_sum(f, -1 * h))
        p2 = shtrassen_multiplication(len(h), matrix_sum(a, b), h)
        p3 = shtrassen_multiplication(len(e), matrix_sum(c, d), e)
        p4 = shtrassen_multiplication(len(d), d, matrix_sum(g, (-1)*e))
        p5 = shtrassen_multiplication(len(a), matrix_sum(a, d), matrix_sum(e, h))
        p6 = shtrassen_multiplication(len(b), matrix_sum(b, -1 * d), matrix_sum(g, h))
        p7 = shtrassen_multiplication(len(a), matrix_sum(a, -1 * c), matrix_sum(e, f))

        width = len(p5[0]) + len(p1[0])
        height = len(p5) + len(p3)

        res = [[0 for _ in range(width)] for _ in range(height)]
        l = matrix_sum(p5, matrix_sum(p4, matrix_sum(-1 * p2, p6)))
        m = matrix_sum(p1, p2)
        p = matrix_sum(p3, p4)
        o = matrix_sum(p1, matrix_sum(p5, matrix_sum(-1 * p3, -1 * p7)))

        for i in range(height // 2):
            for j in range(width // 2):
                res[i][j] = l[i][j]

        for i in range(height // 2):
            for j in range(width // 2, width):
                res[i][j] = m[i][j - width // 2]

        for i in range(height // 2, height):
            for j in range(width // 2):
                res[i][j] = p[i - height // 2][j]

        for i in range(height // 2, height):
            for j in range(width // 2, width):
                res[i][j] = o[i - height // 2][j - width // 2]
        return np.array(res)

    return np.array([x[0] * y[0]])

def matrix_sum(a, b):
    n = len(a)
    c = np.array([[0 for _ in range(n)] for _ in range(n)])
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
    return c

@measure_performance
def base_matmul(n, x, y):
    if n >= 2:
        q = n // 2

        a = np.array([i[:q] for i in x[:q]])
        b = np.array([i[q:] for i in x[:q]])
        c = np.array([i[:q] for i in x[q:]])
        d = np.array([i[q:] for i in x[q:]])

        e = np.array([i[:q] for i in y[:q]])
        f = np.array([i[q:] for i in y[:q]])
        g = np.array([i[:q] for i in y[q:]])
        h = np.array([i[q:] for i in y[q:]])

        # p1 = a * (f - h)
        # p2 = (a + b) * h
        # p3 = (c + d) * e
        # p4 = d * (g - e)
        # p5 = (a + d) * (e + h)
        # p6 = (b - d) * (g + h)
        # p7 = (a - c) * (e + f)

        ae = base_matmul(len(a), a, e)
        bg = base_matmul(len(b), b, g)
        af = base_matmul(len(a), a, f)
        bh = base_matmul(len(b), b, h)
        ce = base_matmul(len(c), c, e)
        dg = base_matmul(len(d), d, g)
        cf = base_matmul(len(c), c, f)
        dh = base_matmul(len(d), d, h)

        width = len(ae[0]) + len(af[0])
        height = len(ae) + len(ce)

        res = [[0 for _ in range(width)] for _ in range(height)]
        l = matrix_sum(ae, bg)
        m = matrix_sum(af, bh)
        p = matrix_sum(ce, dg)
        o = matrix_sum(cf, dh)

        for i in range(height // 2):
            for j in range(width // 2):
                res[i][j] = l[i][j]

        for i in range(height // 2):
            for j in range(width // 2, width):
                res[i][j] = m[i][j - width // 2]

        for i in range(height // 2, height):
            for j in range(width // 2):
                res[i][j] = p[i - height // 2][j]

        for i in range(height // 2, height):
            for j in range(width // 2, width):
                res[i][j] = o[i - height // 2][j - width // 2]
        return np.array(res)

    return np.array([x[0] * y[0]])

if __name__ == "__main__":
    for i in range(1, 11):
        generate_data(i)
        ln, mat1, mat2 = get_data()
        fin = shtrassen_multiplication(ln, mat1, mat2)
        real_res = mat1 @ mat2
        with open('output.txt', 'w') as fl:
            fl.writelines("\n".join(map(str, [" ".join(map(str, row)) for row in fin])))
        base_fin = base_matmul(ln, mat1, mat2)
        assert all([real_res[i][j] == fin[i][j] == base_fin[i][j] for j in range(ln)] for i in range(ln)), 'not equal......'
        print('--' * 50)