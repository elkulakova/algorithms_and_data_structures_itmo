from measurments import *
from random_array import *
from copy import deepcopy


def get_data():
    with open('input.txt') as f:
        data = f.readlines()

    return int(data[0]), list(map(int, data[1].split()))

def find_index():
    global fin_data, init_arr
    res = []
    for tup in fin_data:
        start_index, end_index = None, None
        for i in range(len(init_arr) - len(tup[0]) + 1):
            if init_arr[i:i + len(tup[0])] == tup[0]:
                start_index = i
                end_index = i + len(tup[0]) - 1
                break
        res.append(f'{start_index + 1}, {end_index + 1}, {tup[1]}, {tup[2]}\n')
    return res


@measure_performance
def merge_sort(n, arr):
    data = [deepcopy(arr)]
    global init_arr, fin_data

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
                arr[k + 1:] = r_sorted[j:]
                break
            i += 1
        else:
            arr[k] = r_sorted[j]
            if j == len(r_sorted) - 1:
                arr[k + 1:] = l_sorted[i:]
                break
            j += 1

    data.extend([arr[0], arr[-1]])
    fin_data.append(data)

    return arr

if __name__ == "__main__":
    #generate_array(10)
    init_arr = get_data()[1]
    fin_data = []
    fin_data1 = []
    ln, array = get_data()
    print('started algorithm')
    sarr = merge_sort(ln, array)
    result = find_index()
    result.append(" ".join(map(str, sarr)))
    with open('output.txt', 'w') as fl:
        fl.writelines(result)
    assert sorted(array) == sarr, 'not sorted.....'