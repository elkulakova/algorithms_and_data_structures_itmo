from generator import *
from measurments import *

@measure_performance
def lcs(a, b):
    n = len(a)
    m = len(b)
    table = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        table[i][0] = 0
    for j in range(m+1):
        table[0][j] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i - 1] == b[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table[n][m]

if __name__ == '__main__':
    array_generator()
    with open('input.txt') as f:
        lena = int(f.readline())
        arr_a = list(map(int, f.readline().split()))
        lenb = int(f.readline())
        arr_b = list(map(int, f.readline().split()))
    res = lcs(arr_a, arr_b)
    with open('output.txt', 'w') as f:
        f.write(str(res))
    print(res)