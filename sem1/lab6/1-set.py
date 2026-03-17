from measurments import *
from generator import *
from hash_class import *

@measure_performance
def set_flow(arr):
    s = HashTable()
    res = []
    for c in arr:
        if 'A' in c:
            x = int(c.strip('A '))
            s.insert(x)
        elif 'D' in c:
            x = int(c.strip('D '))
            s.remove(x)
        else:
            x = int(c.strip('? '))
            res.append(s.contains(x))
    return res

if __name__ == "__main__":
    set_generator()
    with open('input.txt') as f:
        num = int(f.readline())
        acts = []
        for _ in range(num):
            acts.append(f.readline())

    result = set_flow(acts)
    with open('output.txt', 'w') as f:
        for x in result:
            f.write(f'{x}\n')
    print(result)