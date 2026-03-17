from measurments import *
from random_array import *

@measure_performance
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
    generate_array(10)
    with open('input.txt') as fl:
        inp = fl.readlines()

    ln, array = inp[0], list(map(int, inp[1].split(',')))

    sort_arr = recursion_insert()
    print(f'INITIAL ARRAY: {array},\nSORTED ARRAY: {sort_arr}')
    with open('input.txt', 'w') as fl:
        fl.writelines([f'{ln}', f'{", ".join(map(str, array))}'])
    assert sorted(array, reverse=True) == sort_arr, 'not sorted!!!!!'