from collections import deque
from measurments import *
from generator import *

@measure_performance
def pack_preproc(arr, buffer_capacity):
    if len(arr) <= 1:
        if len(arr) == 0:
            return []
        else:
            return [arr[0][0]]
    cur_time = 0
    deq = deque()
    process_start = [None] * len(arr)

    for i in range(len(arr)):
        a = arr[i]
        if len(deq) < buffer_capacity:
            deq.append((a, i))
            #print(f'added: {deq}')
        else:
            #print(f'current time: {cur_time}')
            if cur_time < deq[0][0][0]:
                cur_time = deq[0][0][0]
            process_start[deq[0][1]] = cur_time
            #print(f'processed start: {process_start}')
            cur_time += deq[0][0][1]
            #print(f'current time after processing {deq[0][0]}: {cur_time}')
            deq.popleft()
            if cur_time > a[0]:
                process_start[i] = -1 ###
                #print(f'missed start: {process_start} for {a}, print {cur_time}')
            else:
                deq.append((a, i))
            #print(f'deq now {deq}')

    while deq:
        if cur_time < deq[0][0][0]:
            cur_time = deq[0][0][0]
        process_start[deq[0][1]] = cur_time
        #print(f'processed start (fin): {process_start}')
        cur_time += deq[0][0][1]
        deq.popleft()

    return process_start

if __name__ == '__main__':
    #packages_generator(1, 1)
    with open('input.txt') as f:
        bc, n = tuple(map(int, f.readline().split()))
        packs = []
        for _ in range(n):
            num, time = tuple(map(int, f.readline().split()))
            packs.append((num, time))

    #print(packs)
    res = pack_preproc(packs, bc)
    with open('output.txt', 'w') as f:
        f.write("\n".join(map(str, res)))
    #print(res)