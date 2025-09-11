def summa():
    a, b = map(int, input().split())
    return a + b


def sum_square():
    a, b = map(int, input().split())
    return a + b**2


def sum_file():
    in_file, out_file = map(str, input().split())
    with open(in_file) as f:
        a, b = map(int, f.readline().split())

    with open(out_file, 'w') as f:
        f.write(str(a + b))

    return a + b


def sum_square_file():
    in_file, out_file = map(str, input().split())
    with open(in_file) as f:
        a, b = map(int, f.readline().split())

    with open(out_file, 'w') as f:
        f.write(str(a + b**2))

    return a + b**2


print(sum_square_file())
