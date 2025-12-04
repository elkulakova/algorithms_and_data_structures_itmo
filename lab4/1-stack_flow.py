from stack_class import *
from generate_commands import *
from measurments import *

@measure_performance
def stack_flow(n, cmnds):
    my_stack = Stack(10**6)
    popped = []
    for cmnd in cmnds:
        if cmnd == '-':
            popped.append(my_stack.pop())
        else:
            val = int(cmnd.strip('+ '))
            my_stack.push(val)
    return popped

if __name__ == "__main__":
    generate_cmnds()
    with open('input.txt') as f:
        n = int(f.readline())
        commands = []
        for i in range(n):
            commands.append(f.readline().strip())

    res = stack_flow(n, commands)
    with open('output.txt', 'w') as f:
        for r in res:
            f.write(f'{str(r)}\n')