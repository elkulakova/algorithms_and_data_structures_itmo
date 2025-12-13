from gems_additional_classes import *
from lab6.generator import gems_generator
from measurments import *

@measure_perf
def beautiful_pairs(gems, pairs_list):
    ht = BeautifulHashTable(gems)
    return ht.count_pairs(pairs_list)

if __name__ == "__main__":
    gems_generator()
    with open('input.txt') as f:
        n, k = map(int, f.readline().split())
        gems_str = f.readline().strip()
        pairs = []
        for _ in range(k):
            p = list(f.readline().strip())
            pairs.append(tuple(p))
    res = beautiful_pairs(gems_str, pairs)
    with open('output.txt', 'w') as f:
        f.write(str(res))
    print(res)