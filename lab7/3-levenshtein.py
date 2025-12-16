from generator import *
from measurments import *
from numba import jit

@measure_performance
def lev_dist(init_word, res_word):
    n = len(init_word)
    m = len(res_word)
    if n == 0:
        return m
    if m == 0:
        return n
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = max(i, j)
            else:
                if init_word[i-1] == res_word[j-1]:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1])
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)

    return dp[n][m]

@measure_perf
@jit(nopython=True)
def ld_fast(a, b):
    if len(a) < len(b):
        a, b = b, a

    n, m = len(a), len(b)
    prev = list(range(m + 1))
    curr = [0] * (m + 1)

    for i in range(1, n + 1):
        curr[0] = i
        ai = a[i - 1]

        for j in range(1, m + 1):
            cost = 0 if ai == b[j - 1] else 1

            x = prev[j] + 1
            y = curr[j - 1] + 1
            z = prev[j - 1] + cost

            if x > y:
                x = y
            if x > z:
                x = z

            curr[j] = x

        prev, curr = curr, prev

    return prev[m]

@measure_performance
def ld_fast1(a, b):
    if len(a) < len(b):
        a, b = b, a

    n, m = len(a), len(b)
    prev = list(range(m + 1))
    curr = [0] * (m + 1)

    for i in range(1, n + 1):
        curr[0] = i
        ai = a[i - 1]

        for j in range(1, m + 1):
            cost = 0 if ai == b[j - 1] else 1

            x = prev[j] + 1
            y = curr[j - 1] + 1
            z = prev[j - 1] + cost

            if x > y:
                x = y
            if x > z:
                x = z

            curr[j] = x

        prev, curr = curr, prev

    return prev[m]

@measure_performance
def lev_dist_with_ops(init_word, res_word):
    n, m = len(init_word), len(res_word)

    if n == 0:
        return m, [f"add {c}" for c in res_word]
    if m == 0:
        return n, [f"del {c}" for c in init_word]

    # Матрица расстояний
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    # Матрица операций (для восстановления пути)
    ops = [[None] * (m + 1) for _ in range(n + 1)]

    # Инициализация
    for i in range(n + 1):
        dp[i][0] = i
        ops[i][0] = 'del'
    for j in range(m + 1):
        dp[0][j] = j
        ops[0][j] = 'add'

    # Заполняем матрицы
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if init_word[i - 1] == res_word[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                ops[i][j] = 'match'
            else:
                candidates = [
                    (dp[i - 1][j] + 1, 'del'),
                    (dp[i][j - 1] + 1, 'add'),
                    (dp[i - 1][j - 1] + 1, 'change')
                ]
                min_val, op = min(candidates)
                dp[i][j] = min_val
                ops[i][j] = op

    # Восстанавливаем операции (обратный проход)
    operations = []
    i, j = n, m

    while i > 0 or j > 0:
        op = ops[i][j]

        if op == 'match':
            i -= 1
            j -= 1
        elif op == 'del':
            operations.append(f"del {init_word[i - 1]}")
            i -= 1
        elif op == 'add':
            operations.append(f"add {res_word[j - 1]}")
            j -= 1
        elif op == 'change':
            operations.append(f"change {init_word[i - 1]} {res_word[j - 1]}")
            i -= 1
            j -= 1

    return dp[n][m], operations


if __name__ == '__main__':
    #levenshtein_generator()
    with open('input.txt') as f:
        initial_val = f.readline().strip()
        result_val = f.readline().strip()
    res, ops = lev_dist_with_ops(initial_val, result_val)
    #_ = ld_fast1(initial_val, result_val)
    with open('output.txt', 'w') as f:
        f.write(f'{res}')
        for op in ops:
            f.write(f'\n{op}')
    print(res)
    #print(ld('short', 'ports'))