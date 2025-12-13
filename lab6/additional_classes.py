import random

def partition3(A, l, r):
    x = A[l]
    lt = l
    gt = r
    i = l
    while i <= gt:
        if A[i] < x:
            A[lt], A[i] = A[i], A[lt]
            lt += 1
            i += 1
        elif A[i] > x:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1
    return lt, gt

def randomized_quick_sort(A, l, r):
    if l < r:
        k = random.randint(l, r)
        A[l], A[k] = A[k], A[l]
        m1, m2 = partition3(A, l, r)
        randomized_quick_sort(A, l, m1 - 1)
        randomized_quick_sort(A, m2 + 1, r)
    return A


class HashVotesTable:
    def __init__(self):
        self.m = 2000003
        self.table = [None] * self.m

    def h1(self, key):
        p, m = 31, self.m
        h = 0
        for c in key:
            h = (h * p + ord(c))
        return h % m

    def hash_func(self, x, k):
        return (self.h1(x) + k * 37) % self.m

    def _search(self, srnm):
        i = 0
        while i < self.m:
            j = self.hash_func(srnm, i)
            if self.table[j] is None:
                return j, False
            elif self.table[j][0] == srnm:
                return j, True
            i += 1
        return -1, False

    def insert(self, srnm, votes):
        j, exist = self._search(srnm)
        if j == -1:  # Переполнение
            raise OverflowError
        if exist:
            fin_votes = self.table[j][1] + votes
            self.table[j] = (srnm, fin_votes)
        else:
            self.table[j] = (srnm, votes)

    def get_results(self):
        cands = [tup for tup in self.table if isinstance(tup, tuple)]
        return randomized_quick_sort(cands, 0, len(cands) - 1)