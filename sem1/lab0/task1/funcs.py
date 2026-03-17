def summa():
    a, b = map(int, input().split())
    return a + b


def sum_square():
    a, b = map(int, input().split())
    return a + b**2


def sum_file():
    with open('input.txt') as f:
        a, b = map(int, f.readline().split())

    with open('output.txt', 'w') as f:
        f.write(str(a + b))

    return a + b


def sum_square_file():
    with open('input.txt') as f:
        a, b = map(int, f.readline().split())

    with open('output.txt', 'w') as f:
        f.write(str(a + b**2))

    return a + b**2

if __name__ == "__main__":
    print(sum_square_file())