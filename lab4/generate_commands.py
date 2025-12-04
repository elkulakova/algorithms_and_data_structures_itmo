import random
import numpy as np

def generate_cmnds(size=None):
    if size is None:
        size = random.randint(1, 10**6)

    cmds = []
    stack_size = 0

    for _ in range(size):
        # если стек пуст, можем только пушнуть
        if stack_size == 0:
            x = random.randint(-10 ** 9, 10 ** 9)
            cmds.append(f"+ {x}")
            stack_size += 1
        else:
            # иначе случайно выбираем, пуш или поп
            if random.random() < 0.75:  # вероятность пуша
                x = random.randint(-10 ** 9, 10 ** 9)
                cmds.append(f"+ {x}")
                stack_size += 1
            else:
                cmds.append("-")
                stack_size -= 1

    with open('input.txt', 'w') as f:
        f.write(str(size) + "\n")
        f.write("\n".join(cmds))

    return None

def build_commands(n=None, m=None):
    if not n:
        n = random.randint(1, 75000)
    if not m:
        m = random.randint(1, 75000)

    in_line = {1}
    in_crowd = set(range(2, n + 1))

    cmds = []

    for _ in range(m):
        can_leave = len(in_line) > 1

        cmd_type = random.random()
        if cmd_type < 0.4 and in_crowd:
            i = random.choice(list(in_crowd))
            j = random.choice(list(in_line))
            if random.random() < 0.5:
                cmds.append(f"left {i} {j}")
            else:
                cmds.append(f"right {i} {j}")
            in_crowd.remove(i)
            in_line.add(i)

        elif cmd_type < 0.7 and can_leave:
            i = random.choice(list(in_line))
            if len(in_line) > 1:
                cmds.append(f"leave {i}")
                in_line.remove(i)
                in_crowd.add(i)
            else:
                i = random.choice(list(in_line))
                cmds.append(f"name {i}")

        else:
            i = random.choice(list(in_line))
            cmds.append(f"name {i}")

    with open("input.txt", "w") as f:
        f.write(f"{n} {m}\n")
        f.write("\n".join(cmds))

    return None