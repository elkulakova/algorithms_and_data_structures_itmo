from measurments import measure_memory_usage, timeit
from create_arrays import *

def get_data():
    with open('input.txt') as f:
        data = f.readlines()
    n, arr1, k, arr2 = int(data[0]), list(map(int, data[1].split())), int(data[2]), list(map(int, data[3].split()))
    return n, arr1, k, arr2

lena = get_data()[0]
a = get_data()[1]
etz = [0 for _ in range(lena)]
#print(lena, a)

def eytzinger(q, k=0):
    global etz, a, lena
    print(k, lena, etz, q)
    if k < lena:
        etz[k] = a[q]
        eytzinger((q // 2), 2*k+1)
        eytzinger((q // 2) + (lena // 2), 2*k+2)

@measure_performance
def etz_search(n, arr):
    global etz
    eytzinger(n // 2)
    t = etz
    res_arr = []
    for j in arr:
        k = 0
        while k < n:
            k = 2*k + (t[k] < j) + 1
        k >> (k & -k).bit_length()
        res_arr.append(t[k])
        #print(res_arr)
    return res_arr


if __name__ == "__main__":
    #generate_arrays(10**5, 10**5)
    ln, arra, lk, arrb = get_data()

    res = etz_search(ln, arrb)
    print("Found indices:", res)
