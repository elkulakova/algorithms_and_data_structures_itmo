from measurments import *
from random_array import *

@measure_memory_usage
@timeit
def linear_search():
    with open('input.txt') as f:
        data = f.readlines()

    arr, v = list(map(str, data[0].split())), str(data[1])

    v_inds = []

    if len(arr) < 2:
        if len(arr) == 0:
            v_inds = []
        else:
            if arr[0] == v:
                v_inds.append(0)
            else:
                v_inds = []
    else:
        for i in range(len(arr)):
            if v == arr[i]:
                v_inds.append(i)

    output = f'{", ".join(map(str, v_inds))}'.strip(', ') if v_inds else str(-1)
    with open('output.txt', 'w') as f:
        if len(v_inds) > 1:
            f.writelines([f'{len(v_inds)}\n', output])
        else:
            f.write(output)
    return output

if __name__ == "__main__":
    generate_array(1000)
    res = linear_search()
    with open('input.txt') as fl:
        d = fl.readlines()
    array, val = list(map(str, d[0].split())), str(d[1]).strip()
    indices = [i for i, x in enumerate(array) if x == val]
    inds = f'{", ".join(map(str, indices))}'.strip(', ') if indices else str(-1)
    assert inds == res, 'bad((('
    print(res)