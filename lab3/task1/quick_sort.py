from measurments import *
from random_array import *
import random

def partition(A, l, r):
    x = A[l]
    j = l
    for i in range(l+1, r+1):
        if A[i] <= x:
            j += 1
            A[j], A[i] = A[i], A[j]
    A[l], A[j] = A[j], A[l]
    return j

@measure_performance
def quick_sort(A, l, r):
    if l < r:
        m = partition(A, l, r)
        quick_sort(A, l, m-1)
        quick_sort(A, m+1, r)
    return A

if __name__ == "__main__":
    generate_array(10**4, 'desc')
    with open('input.txt') as f:
        n, arr = int(f.readline()), list(map(int, f.readline().split()))

    sarr = quick_sort(arr, 0, len(arr) - 1)
    assert all([sorted(arr)[i] == sarr[i] for i in range(len(arr))]), 'not sorted......'
    with open('output.txt', 'w') as f:
        f.write(" ".join(map(str, sarr)))
    #print(sarr)
