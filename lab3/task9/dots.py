from generate_dots import *
from measurments import *
import random

def partition3(A, l, r, by='x'):
    if by == 'x':
        coord = 0
    else:
        coord = 1
    x = A[l][coord]
    lt = l
    gt = r
    i = l
    while i <= gt:
        if A[i][coord] < x:
            A[lt], A[i] = A[i], A[lt]
            lt += 1
            i += 1
        elif A[i][coord] > x:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1
    return lt, gt

def randomized_quick_sort(A, l, r, by='x'):
    if l < r:
        k = random.randint(l, r)
        A[l], A[k] = A[k], A[l]
        m1, m2 = partition3(A, l, r, by=by)
        randomized_quick_sort(A, l, m1 - 1, by)
        randomized_quick_sort(A, m2 + 1, r, by)
    return A

def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

@measure_base_performance
def min_distance(n, dots):
    # сортировка по иксам => делим пополам => рекурсивно ищем минимальное расстояние в левой и правой части
    # потом ищем минимальное расстояние между точками, которые лежат на расстоянии min_dist и меньше от середины
    if n <= 3:
        md = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                md = min(md, dist(dots[i], dots[j]))
        return md

    sorted_dots = randomized_quick_sort(dots[:], 0, n - 1)
    mid_x = sorted_dots[n // 2][0]
    dl = min_distance(n//2, sorted_dots[:n//2])
    dr = min_distance(n//2, sorted_dots[n//2:])
    d = min(dl, dr)

    narrowed_dots = [point for point in sorted_dots if abs(point[0] - mid_x) < d]
    n_nd = len(narrowed_dots)
    sorted_ndots = randomized_quick_sort(narrowed_dots, 0, n_nd - 1, 'y')
    md = float('inf')
    for i in range(n_nd):
        for j in range(i + 1, min(i + 8, n_nd)):
            md = min(md, dist(sorted_ndots[i], sorted_ndots[j]))
            if md < d:
                break

    min_dist = min(md, d)
    return min_dist

if __name__ == '__main__':
    generate_dots(10**5)
    with open('input.txt') as f:
        n = int(f.readline())
        dots = [tuple(map(int, f.readline().split())) for _ in range(n)]

    res = min_distance(n, dots)
    with open ('output.txt', 'w') as f:
        f.write(str(res))

    print(f"{res:.6f}")