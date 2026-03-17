from generator import *
from measurments import *

@measure_perf
def template(tmplt, strk):
    compressed = []
    for c in tmplt:
        if c == '*' and compressed and compressed[-1] == '*':
            continue
        compressed.append(c)
    tmplt = ''.join(compressed)

    n, m = len(tmplt), len(strk)
    dp = [False] * (m + 1)
    dp[0] = True

    for i in range(1, n + 1):
        new_dp = [False] * (m + 1)
        if tmplt[i - 1] == '*':
            reached = False
            for j in range(m + 1):
                reached = reached or dp[j]
                new_dp[j] = reached
        else:
            for j in range(1, m + 1):
                if tmplt[i - 1] == '?':
                    new_dp[j] = dp[j - 1]
                else:
                    new_dp[j] = dp[j - 1] and tmplt[i - 1] == strk[j - 1]
        dp = new_dp

    return 'YES' if dp[m] else 'NO'

@measure_performance
def template_two_pointer(tmplt, strk):
    i = j = 0
    star_idx = -1   # индекс последнего * в шаблоне
    match = 0       # индекс в строке, с которого * начинает покрывать

    n, m = len(tmplt), len(strk)

    while j < m:
        if i < n and (tmplt[i] == strk[j] or tmplt[i] == '?'):
            i += 1
            j += 1
        elif i < n and tmplt[i] == '*':
            star_idx = i
            match = j
            i += 1
        elif star_idx != -1:
            # возвращаемся к первому после * элементу, растягиваем его на один символ
            i = star_idx + 1
            match += 1
            j = match
        else:
            return 'NO'

    # проверяем остаток шаблона (может быть несколько * в конце)
    while i < n and tmplt[i] == '*':
        i += 1

    return 'YES' if i == n else 'NO'

@measure_perf
def matches(pattern, filename):
    m = len(filename)
    n = len(pattern)
    dp = [[False for _ in range(m+1)] for _ in range(n+1)]

    dp[0][0] = True
    for j in range(1, n+1):
        if pattern[j-1] == '*':
            dp[0][j] = dp[0][j-1]

    for j in range(1, n+1):
        for i in range(1, m+1):
            if pattern[j-1] == '*':
                dp[i][j] = dp[i][j-1] or dp[i-1][j]
            elif pattern[j-1] == '?' or pattern[j-1] == filename[i-1]:
                dp[i][j] = dp[i-1][j-1]

    return "YES" if dp[n][m] else "NO"

if __name__ == '__main__':
    generate_template_and_string()
    with open('input.txt') as f:
        temp = f.readline().strip()
        stroka = f.readline().strip()
    res = template_two_pointer(temp, stroka)
    with open('output.txt', 'w') as f:
        f.write(res)