from measurments import *
from random_array import *

@measure_performance
def get_data():
    with open('input.txt') as f:
        data = f.readlines()

    return int(data[0]), list(map(int, data[1].split()))

init_arr = get_data()[1]
fin_data = []

def merge_sort(n, arr):
    global init_arr, fin_data

    start_index, end_index = None, None
    for i in range(len(init_arr) - len(arr) + 1):
        if init_arr[i:i + len(arr)] == arr:
            start_index = i
            end_index = i + len(arr) - 1
            break

    if n == 1:
        return arr
    l_arr = arr[:n//2]
    r_arr = arr[n//2:]
    l_sorted = merge_sort(len(l_arr), l_arr)
    r_sorted = merge_sort(len(r_arr), r_arr)

    i, j = 0, 0
    for k in range(n):
        if l_sorted[i] >= r_sorted[j]:
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

    fin_data.append(f'{start_index + 1}, {end_index + 1}, {arr[0]}, {arr[-1]}\n')
    return arr

if __name__ == "__main__":
    #generate_array(10, pattern='asc')
    ln, array = get_data()
    print(f'INITIL ARRAY: {array}')
    sarr = merge_sort(ln, array)
    fin_data.append(" ".join(map(str, sarr)))
    with open('output.txt', 'w') as fl:
        fl.writelines(fin_data)
    assert sorted(array, reverse=True) == sarr, 'not sorted.....'