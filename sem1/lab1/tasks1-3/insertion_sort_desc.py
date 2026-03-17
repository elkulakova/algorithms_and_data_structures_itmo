from measurments import *
from random_array import *

@measure_memory_usage
@timeit
def sort_desc_insert():
    with open('input.txt') as f:
        data = f.readlines()

    n, arr = int(data[0]), list(map(int, data[1].split(',')))

    if n > 1:
        for i in range(1, n):
            current = arr[i]
            pos = i

            while pos > 0 and arr[pos - 1] < current:
                arr[pos], arr[pos - 1] = arr[pos - 1], arr[pos]
                pos -= 1

    with open('output.txt', 'w') as f:
        f.write(" ".join(map(str, arr)))
    return arr

if __name__ == "__main__":
    generate_array(1000)
    with open('input.txt') as f:
        inp = f.readlines()
    array = list(map(int, inp[1].split(',')))
    my_arr = sort_desc_insert()
    print(my_arr)
    assert sorted(array, reverse=True) == my_arr, 'not sorted!'