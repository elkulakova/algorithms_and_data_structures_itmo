from measurments import *
from generator import *

@measure_performance
def heap_min_identifier(arr, n):
    for i in range((n-2)//2 + 1):
        l = 2*i + 1
        r = 2*i + 2

        if l < n and arr[i] > arr[l]:
            return 'NO'
        if r < n and arr[i] > arr[r]:
            return 'NO'

    return 'YES'

@measure_performance
def heap_max_identifier(arr, n):
    for i in range((n-2)//2 + 1):
        l = 2*i + 1
        r = 2*i + 2

        if l < n and arr[i] < arr[l]:
            return 'NO'
        if r < n and arr[i] < arr[r]:
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    heap_generator()
    with open('input.txt') as f:
        n = int(f.readline())
        items = list(map(int, f.readline().split()))

    #print(items, n)
    res_min = heap_min_identifier(items, n)
    res_max = heap_max_identifier(items, n)
    with open('output.txt', 'w') as f:
        f.write(res_min)
    print(res_min, res_max)