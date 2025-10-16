from measurments import *
from random_array import *
from numpy import inf

@measure_performance
def get_data():
    with open('input.txt') as f:
        data = f.readlines()

    return int(data[0]), list(map(int, data[1].split()))

def merge(arr, p, q, r):
    n1 = q - p
    n2 = r - q
    lft = [0 for _ in range(n1 + 1)]
    rght = [0 for _ in range(n2 + 1)]

    # lft[:n1] = arr[:q]
    # rght[:n2] = arr[q:]

    for i in range(n1):
        lft[i] = arr[p+i]
    for j in range(n2):
        rght[j] = arr[q+j]

    lft[-1] = inf
    rght[-1] = inf
    i, j = 0, 0

    for k in range(p, r):
        if lft[i] <= rght[j]:
            arr[k] = lft[i]
            i += 1
        else:
            arr[k] = rght[j]
            j += 1

    return arr

def merge_sort(arr, p, r):
    if p < r - 1:
        q = (p+r)//2
        merge_sort(arr, p, q)
        merge_sort(arr, q, r)
        return merge(arr, p, q, r)
    return arr

if __name__ == "__main__":
    #generate_array(2*10000, 'asc')
    ln, array = get_data()
    #print(f'INITIAL ARRAY:{array}')
    sarr = merge_sort(array, 0, ln)

    with open('output.txt', 'w') as fl:
        fl.write(" ".join(map(str, sarr)))

    assert sorted(array) == sarr, 'not sorted.....'
    #print(sarr)