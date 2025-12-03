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

def brute_force(points):
    n = len(points)
    best = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            d = dist(points[i], points[j])
            if d < best:
                best = d
    return best

def closest_pair_rec(Px, Py):
    n = len(Px)
    if n <= 3:
        return brute_force(Px)

    mid = n // 2
    mid_x = Px[mid][0]

    Qx = Px[:mid]
    Rx = Px[mid:]

    Qy = []
    Ry = []
    for p in Py:
        if p[0] <= mid_x:
            Qy.append(p)
        else:
            Ry.append(p)

    dl = closest_pair_rec(Qx, Qy)
    dr = closest_pair_rec(Rx, Ry)
    d = min(dl, dr)

    strip = [p for p in Py if abs(p[0] - mid_x) < d]

    best = d
    m = len(strip)
    for i in range(m):
        j = i + 1
        while j < m and (strip[j][1] - strip[i][1]) < best and j <= i + 7:
            d_ij = dist(strip[i], strip[j])
            if d_ij < best:
                best = d_ij
            j += 1

    return best

@measure_base_performance
def closest_pair(points):
    Px = randomized_quick_sort(points[:], 0, len(points) - 1)
    Py = randomized_quick_sort(points[:], 0, len(points) - 1, by='y')
    return closest_pair_rec(Px, Py)

if __name__ == '__main__':
    #generate_dots()
    with open('input.txt') as f:
        n = int(f.readline())
        dots = [tuple(map(int, f.readline().split())) for _ in range(n)]

    res = closest_pair(dots)
    with open ('output.txt', 'w') as f:
        f.write(f"{res:.6f}")

    print(f"{res:.6f}")