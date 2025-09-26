from measurments import *
from random_array import *

@measure_memory_usage
@timeit
def sort_insert():
    with open('input.txt') as f:
        data = f.readlines()

    n, arr = int(data[0]), list(map(int, data[1].split(',')))

    index_array = [1]
    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
        index_array.append(j+1)

    with open('output.txt', 'w') as f:
        f.writelines([f'{" ".join(map(str, index_array))}\n', " ".join(map(str, arr))])

    return arr

if __name__ == "__main__":
    sort_insert()