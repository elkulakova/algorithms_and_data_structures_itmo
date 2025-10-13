from measurments import *
from random_array import *

@measure_memory_usage
@timeit
def recursion_insert():
    with open('input.txt') as f:
        data = f.readlines()

    n, init_arr = int(data[0]), list(map(int, data[1].split(',')))

    if n <= 1:
        return init_arr

    k = init_arr[-1]
    with open('input.txt', 'w') as f:
        f.write(f'{str(n-1)}\n')
        f.write(", ".join(map(str, init_arr[:-1])))
    arr = recursion_insert()
    arr.append(k)

    i = n - 2
    while arr[i] > arr[i+1] and i > 0:
        i -= 1

    while i >= 0 and arr[i + 1] > arr[i]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        i -= 1

    with open('output.txt', 'w') as f:
        f.write(" ".join(map(str, arr)))
    return arr

if __name__ == "__main__":
    generate_array(15)
    with open('input.txt') as f:
        data = f.readlines()

    _, init_arr = int(data[0]), list(map(int, data[1].split(',')))

    sort_arr = recursion_insert()
    print(f'INITIAL ARRAY: {init_arr},\nSORTED ARRAY: {sort_arr}')
    assert sorted(init_arr, reverse=True) == sort_arr, 'not sorted!!!!!'