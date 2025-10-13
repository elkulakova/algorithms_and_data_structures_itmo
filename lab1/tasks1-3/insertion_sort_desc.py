from measurments import *
from random_array import *

@measure_memory_usage
@timeit
def sort_desc_insert():
    with open('input.txt') as f:
        data = f.readlines()

    n, arr = int(data[0]), list(map(int, data[1].split(',')))

    if len(arr) > 1:
        sort_success = False
        while not sort_success:
            j = n - 1
            while j >= 0 and arr[j - 1] >= arr[j]:
                j -= 1
                if j > 0:
                    continue
                else:
                    sort_success = True
            while j > 0 and arr[j - 1] < arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                j -= 1

    with open('output.txt', 'w') as f:
        f.write(" ".join(map(str, arr)))
    return arr

if __name__ == "__main__":
    sort_desc_insert()