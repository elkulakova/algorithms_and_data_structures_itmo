from stack_class import *
from random_commands import *
from measurments import *

@measure_performance
def stack_mix(n, cmnds):
    my_stack = Stack(n)
    maxs = []
    for cmnd in cmnds:
        if cmnd == 'max':
            maxs.append(my_stack.max)
        else:
            if cmnd == 'pop':
                my_stack.pop()
            else:
                val = int(cmnd.strip('push '))
                my_stack.push(val)
    return maxs

if __name__ == "__main__":
    #generate_cmnds()
    with open('input.txt') as f:
        n = int(f.readline())
        commands = []
        for i in range(n):
            commands.append(f.readline().strip())

    res = stack_mix(n, commands)
    with open('output.txt', 'w') as f:
        for r in res:
            f.write(f'{str(r)}\n')
    print(res)