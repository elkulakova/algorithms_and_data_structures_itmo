from measurments import measure_performance
from random_array import *

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

@measure_performance
def find_hirsh_index(arr):
    if not arr:
        return 0

    sarr = randomized_quick_sort(arr, 0, len(arr) - 1)
    ind = 0
    for i in range(len(sarr)):
        if sarr[i] >= len(sarr) - i:
            return len(sarr) - i
    return ind

if __name__ == '__main__':
    generate_array()
    with open('input.txt') as f:
        new_arr = list(map(int, f.readline().split()))

    indx = find_hirsh_index(new_arr)
    with open('output.txt', 'w') as f:
        f.write(str(indx))