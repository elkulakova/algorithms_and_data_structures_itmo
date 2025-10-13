from measurments import *
from random_array import *

@measure_memory_usage
@timeit
def linear_search():
    with open('input.txt') as f:
        data = f.readlines()

    arr, v = list(map(int, data[0].split())), int(data[1])

    v_inds = []
    for i in range(len(arr)):
        if v == arr[i]:
            v_inds.append(i)

    output = f'{", ".join(map(str, v_inds))}'.strip(', ') if v_inds else str(-1)
    with open('output.txt', 'w') as f:
        if len(v_inds) > 1:
            f.writelines([f'{len(v_inds)}\n', output])
        else:
            f.writelines(output)
    return f'{", ".join(map(str, v_inds))}'.strip(', ')

if __name__ == "__main__":
    print(linear_search())