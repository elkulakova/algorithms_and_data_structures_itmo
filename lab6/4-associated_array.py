from measurments import *
from hash_class import *
from generator import *

@measure_performance
def assoc_array(arr, llt):
    result = []
    for v in arr:
        parts = v.strip().split()
        cmd = parts[0]
        if cmd == 'put':
            llt.insert((parts[1], parts[2]))
        elif cmd == 'get':
            result.append(llt.get(parts[1]))
        elif cmd == 'prev':
            result.append(llt.prev(parts[1]))
        elif cmd == 'next':
            result.append(llt.next(parts[1]))
        else:
            llt.remove(parts[1])
    return result

if __name__ == '__main__':
    array_flow(1)
    with open('input.txt') as f:
        n = int(f.readline())
        commands = f.readlines()
    hash_list = HashListTable()
    res = assoc_array(commands, hash_list)
    with open('output.txt', 'w') as f:
        f.write("\n".join(res))
    #print(res)