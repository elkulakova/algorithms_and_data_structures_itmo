from nodelist_class import *
from generate_commands import *
from measurments import *

@measure_performance
def build_flow(cmnds, n):
    line = NodeList(n)
    named = []
    for cmnd in cmnds:
        if 'left' in cmnd:
            vali, valj = tuple(map(int, cmnd.strip('left ').split()))
            line.add_node_left(valj, vali)
        elif 'right' in cmnd:
            vali, valj = tuple(map(int, cmnd.strip('right ').split()))
            line.add_node_right(valj, vali)
        elif 'leave' in cmnd:
            val = int(cmnd.strip('leave '))
            line.remove_node(val)
        elif 'name' in cmnd:
            val = int(cmnd.strip('name '))

            named.append(line.name(val))

    return named

if __name__ == "__main__":
    #build_commands()
    with open('input.txt') as f:
        n, cs = tuple(map(int, f.readline().split()))
        commands = []
        for _ in range(cs):
            commands.append(f.readline())

    res = build_flow(commands, n)
    with open('output.txt', 'w') as f:
        for r in res:
            f.write(" ".join(map(str, r)) + "\n")

    print(res)