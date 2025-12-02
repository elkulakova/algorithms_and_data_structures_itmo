from .measurments import *
from random_array import *
import random

def partition3(A, l, r):
    x = A[l]
    lt = l
    gt = r
    i = l
    while i <= gt:
        if A[i] < x:
            A[lt], A[i] = A[i], A[lt]
            lt += 1
            i += 1
        elif A[i] > x:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1
    return lt, gt

@measure_performance
def randomized_quick_sort(A, l, r):
    if l < r:
        k = random.randint(l, r)
        A[l], A[k] = A[k], A[l]
        m1, m2 = partition3(A, l, r)
        randomized_quick_sort(A, l, m1 - 1)
        randomized_quick_sort(A, m2 + 1, r)
    return A

if __name__ == "__main__":
    generate_array(10**4, pattern='dups')
    with open('input.txt') as f:
        n, arr = int(f.readline()), list(map(int, f.readline().split()))

    sarr = randomized_quick_sort(arr, 0, len(arr) - 1)
    assert all([sorted(arr)[i] == sarr[i] for i in range(len(arr))]), 'not sorted......'
    with open('output.txt', 'w') as f:
        f.write(" ".join(map(str, sarr)))
