def min_heapify(arr, ind, n=None):
    n = len(arr) if n is None else n
    l = 2*ind + 1
    r = 2*ind + 2

    m = ind
    if l < n and arr[ind] > arr[l]:
        m = l
    if r < n and arr[m] > arr[r]:
        m = r

    if m != ind:
        arr[ind], arr[m] = arr[m], arr[ind]
        min_heapify(arr, m, n)


def build_min_heap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        min_heapify(arr, i)

def min_heapsort(arr):
    build_min_heap(arr)
    n = len(arr)
    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        min_heapify(arr, 0, i)
    return arr

class PriorityQueue:
    def __init__(self, flows):
        self.heap = [(0, i) for i in range(flows)]
        self.build_min_heap()

    def build_min_heap(self):
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.min_heapify(i)

    def min_heapify(self, ind, n=None):
        arr = self.heap
        n = len(arr) if n is None else n
        l = 2 * ind + 1
        r = 2 * ind + 2

        m = ind
        if l < n and arr[ind] > arr[l]:
            m = l
        if r < n and arr[m] > arr[r]:
            m = r

        if m != ind:
            arr[ind], arr[m] = arr[m], arr[ind]
            self.min_heapify(m)

    def get_min(self):
        time, flow_num = self.heap[0]
        return time, flow_num

    def increase_min(self, time):
        flow = self.heap[0][1]
        self.heap[0] = (time, flow)
        self.min_heapify(0)
