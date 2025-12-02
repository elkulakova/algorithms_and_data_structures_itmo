from random_array import *
from lab3.task1.rand_qs_part3 import randomized_quick_sort

def find_hirsh_index(arr):
    if not arr:
        return 0

    sarr = randomized_quick_sort(arr, 0, len(arr) - 1)
    print(sarr)
    ind = 0
    for i in range(len(sarr)):
        print(ind, sarr[i], sarr[i:], len(sarr[i:]))
        if sarr[i] >= len(sarr) - i:
            return len(sarr) - i
    return ind

if __name__ == '__main__':
    #generate_array(1)
    with open('input.txt') as f:
        n, new_arr = int(f.readline()), list(map(int, f.readline().split()))
        print(new_arr)

    indx = find_hirsh_index(new_arr)
    print(indx)