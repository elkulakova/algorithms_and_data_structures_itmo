from random_array import *
from measurments import *

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

def randomized_quick_sort(A, l, r):
    if l < r:
        k = random.randint(l, r)
        A[l], A[k] = A[k], A[l]
        m1, m2 = partition3(A, l, r)
        randomized_quick_sort(A, l, m1 - 1)
        randomized_quick_sort(A, m2 + 1, r)
    return A

@measure_base_performance
def scare_sort(arr, n, k):
    sarr = randomized_quick_sort(arr[:], 0, len(arr) - 1)
    if n < k:
        if arr == sarr:
            return 'yes'
        return 'no'
    for r in range(k):
        scared = randomized_quick_sort(arr[r::k], 0, len(arr[r::k]) - 1)
        if scared != sarr[r::k]:
            return 'no'
    return 'yes'

if __name__ == "__main__":
    generate_array()
    with open('input.txt') as f:
        n, k = tuple(map(int, f.readline().split()))
        arr = list(map(int, f.readline().split()))

    res = scare_sort(arr, n, k)
    with open('output.txt', 'w') as f:
        f.write(res)
    print(res)