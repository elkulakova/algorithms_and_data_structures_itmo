from measurments import *
from random_array import *

@measure_performance
def get_data():
    with open('input.txt') as f:
        data = f.readlines()

    return int(data[0]), list(map(int, data[1].split()))

def merge_sort(n, arr):
    if n == 1:
        return arr
    l_arr = arr[:n//2]
    r_arr = arr[n//2:]
    l_sorted = merge_sort(len(l_arr), l_arr)
    r_sorted = merge_sort(len(r_arr), r_arr)

    i, j = 0, 0
    for k in range(n):
        if l_sorted[i] <= r_sorted[j]:
            arr[k] = l_sorted[i]
            if i == len(l_sorted) - 1:
                arr[k+1:] = r_sorted[j:]
                break
            i += 1
        else:
            arr[k] = r_sorted[j]
            if j == len(r_sorted) - 1:
                arr[k+1:] = l_sorted[i:]
                break
            j += 1
    return arr

if __name__ == "__main__":
    generate_array(10, pattern='asc')
    ln, array = get_data()
    sarr = merge_sort(ln, array)
    with open('output.txt', 'w') as fl:
        fl.write(" ".join(map(str, sarr)))
    assert sorted(array) == sarr, 'not sorted.....'