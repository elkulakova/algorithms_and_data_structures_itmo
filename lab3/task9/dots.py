from generate_dots import *
from .measurments import *
import random

def partition3(A, l, r):
    x = A[l][0]
    lt = l
    gt = r
    i = l
    while i <= gt:
        if A[i][0] < x:
            A[lt], A[i] = A[i], A[lt]
            lt += 1
            i += 1
        elif A[i][0] > x:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1
    return lt, gt

@measure_performance
def randomized_quick_sort(A, l, r):
    if l < r:
        k = random.randint(l, r)
        A[l], A[k] = A[k], A[l]
        m1, m2 = partition3(A, l, r)
        randomized_quick_sort(A, l, m1 - 1)
        randomized_quick_sort(A, m2 + 1, r)
    return A


def min_distance(n, dots):
    # сортировка по иксам => делим пополам => рекурсивно ищем минимальное расстояние в левой и правой части
    # потом ищем минимальное расстояние между точками, которые лежат на расстоянии min_dist и меньше от середины
    if n < 2:
        if n == 0:
            return 0.0
        a, b = dots[0], dots[1]
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
    dots = randomized_quick_sort(dots, 0, n - 1)
    min_dist = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            dist = ((dots[i][0] - dots[j][0]) ** 2 + (dots[i][1] - dots[j][1]) ** 2) ** 0.5
            if dist < min_dist:
                min_dist = dist
    return min_dist

if __name__ == '__main__':
    #generate_dots(2)
    with (open('input.txt') as f):
        n = int(f.readline())
        dots = [tuple(map(int, f.readline().split())) for _ in range(n)]

    res = min_distance(n, dots)
    print(f"{res:.6f}")