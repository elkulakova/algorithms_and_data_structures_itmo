from collections import deque
from measurments import *
from random_array import *

@measure_performance
def dynamic_max(arr, n, k):
    dq = deque()
    res = []

    for i in range(n):
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
        dq.append(i)

        if dq[0] <= i - k:
            dq.popleft()

        if i >= k - 1:
            res.append(arr[dq[0]])
    return res

if __name__ == "__main__":
    generate_array()
    with open("input.txt") as f:
        size = int(f.readline())
        array = list(map(int, f.readline().split()))
        window_size = int(f.readline())

    maxs = dynamic_max(array, size, window_size)
    with open("output.txt", "w") as f:
        f.write(" ".join(map(str, maxs)))