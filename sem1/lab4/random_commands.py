import random

def generate_cmnds(size=None):
    if size is None:
        size = random.randint(1, 4 * 10**5)

    cmds = []
    stack_size = 0

    for _ in range(size):
        if stack_size == 0:
            x = random.randint(0, 10 ** 5)
            cmds.append(f"push {x}")
            stack_size += 1
        else:
            if random.random() < 0.75:
                x = random.randint(0, 10 ** 5)
                cmds.append(f"push {x}")
                stack_size += 1
            else:
                if random.random() < 0.5:
                    cmds.append("pop")
                    stack_size -= 1
                else:
                    cmds.append("max")

    with open('input.txt', 'w') as f:
        f.write(str(size) + "\n")
        f.write("\n".join(cmds))

    return None