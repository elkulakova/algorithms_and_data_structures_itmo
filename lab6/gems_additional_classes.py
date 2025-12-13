class BeautifulHashTable:
    def __init__(self, s: str):
        self.s = s
        self.pos = [[] for _ in range(26)]
        self._preprocess()

    def _preprocess(self):
        for idx, ch in enumerate(self.s):
            self.pos[ord(ch) - 97].append(idx)

    def count_pairs(self, queries: list[tuple[str, str]]) -> int:
        ans = 0
        for a, b in queries:
            ia = ord(a) - 97
            ib = ord(b) - 97

            A = self.pos[ia]
            B = self.pos[ib]

            i = 0
            lenA = len(A)

            for bj in B:
                while i < lenA and A[i] < bj:
                    i += 1
                ans += i
        return ans