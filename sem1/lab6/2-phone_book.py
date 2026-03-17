from hash_class import *
from measurments import *
from generator import *

@measure_performance
def phone_book(commands):
    pb = HashTupleTable()
    founds = []
    for command in commands:
        parts = command.strip().split()
        cmd = parts[0]
        if cmd == 'add':
            num = int(parts[1])
            name = ' '.join(parts[2:])
            pb.insert((num, name))
        elif cmd == 'del':
            num = int(parts[1])
            pb.remove(num)
        else:  # find
            num = int(parts[1])
            founds.append(pb.contains(num))
    return founds

if __name__ == '__main__':
    reqs_generator(10**5)
    with open('input.txt') as f:
        n = int(f.readline())
        comms = f.readlines()
    res = phone_book(comms)
    with open('output.txt', 'w') as f:
        f.write('\n'.join(map(str, res)))
    #print(res)