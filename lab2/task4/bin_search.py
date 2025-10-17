from create_arrays import *
from measurments import *

def get_data():
    with open('input.txt') as f:
        data = f.readlines()
    n, arr1, k, arr2 = int(data[0]), list(map(int, data[1].split())), int(data[2]), list(map(int, data[3].split()))
    return n, arr1, k, arr2

#@measure_memory_usage
#@timeit
@measure_base_performance
def binary_search(arr1, arr2):
    a, b = arr1, arr2
    n, k = len(a), len(b)
    inds = [-1] * k

    for i in range(k):
        low, high = 0, n - 1
        j = b[i]

        while low <= high:

            mid = low + ((high - low) >> 1)
            mid_val = a[mid]

            # If x is greater, ignore left half
            if mid_val < j:
                low = mid + 1

            # If x is smaller, ignore right half
            elif mid_val > j:
                high = mid - 1

            # Check if x is present at mid
            else:
                inds[i] = mid
                break
    return inds


if __name__ == "__main__":
    generate_arrays(10**5, 10**5)
    ln, aarr, lk, barr = get_data()
    print('started algorithm')
    result = binary_search(aarr, barr)
    #indices_arr = []

    #fin_arr = binary_search_turbo(aarr, barr)
    #print(f'Array A: {aarr}\nArray B: {barr}\nFOUND INDICES: {fin_arr}')
    #check_arr = [aarr.index(i) if i in aarr else -1 for i in barr]
    #assert all([fin_arr[i] == check_arr[i] for i in range(lk)]), 'wrong......'
