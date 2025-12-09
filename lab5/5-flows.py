from measurments import *
from generator import *
from additional_classes import *

@measure_performance
def flows(tasks_arr, fnum):
    if len(tasks_arr) <= fnum:
        return [(i, 0) for i in range(len(tasks_arr))]
    pq = PriorityQueue(fnum)
    fin_flows = [None] * len(tasks_arr)

    for i in range(len(tasks_arr)):
        t = tasks_arr[i]
        min_time, min_flow = pq.get_min()
        fin_flows[i] = (min_flow, min_time)
        pq.increase_min(min_time + t)

    return fin_flows

if __name__ == '__main__':
    flows_generator()
    with open('input.txt') as f:
        fn, tn = tuple(map(int, f.readline().split()))
        tasks_times = list(map(int, f.readline().split()))

    #print(tasks_times, fn)
    res = flows(tasks_times, fn)
    with open('output.txt', 'w') as f:
        for r in res:
            f.write(f'{" ".join(map(str, r))}\n')
    #print(res)