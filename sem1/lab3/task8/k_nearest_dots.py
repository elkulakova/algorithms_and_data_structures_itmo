from generate_dots import *
from measurments import *
import random

def partition3(A, l, r):
    x = A[l][1]
    lt = l
    gt = r
    i = l
    while i <= gt:
        if A[i][1] < x:
            A[lt], A[i] = A[i], A[lt]
            lt += 1
            i += 1
        elif A[i][1] > x:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1
    return lt, gt

def randomized_quick_sort(A, l, r):
    if l < r:
        k = random.randint(l, r)
        A[l], A[k] = A[k], A[l]
        m1, m2 = partition3(A, l, r)
        randomized_quick_sort(A, l, m1 - 1)
        randomized_quick_sort(A, m2 + 1, r)
    return A

def dist2(p):
    return p[0] ** 2 + p[1] ** 2

@measure_performance
def k_nearest(k, dots, n):
    arr = [(dots[i], dist2(dots[i])) for i in range(n)]
    arr = randomized_quick_sort(arr, 0, n - 1)
    return [p for p, d2 in arr[:k]]

if __name__ == '__main__':
    generate_dots()
    with open('input.txt') as f:
        n, k = tuple(map(int, f.readline().split()))
        dots = [tuple(map(int, f.readline().split())) for _ in range(n)]

    res = k_nearest(k, dots, n)
    towrite = ", ".join(map(str, [f'[{p[0]},{p[1]}]' for p in res]))
    with open ('output.txt', 'w') as f:
        f.write(towrite)