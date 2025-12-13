from additional_classes import *
from lab6.generator import elections_generator
from measurments import *

@measure_performance
def elections(votes_arr):
    ht = HashVotesTable()
    for votes in votes_arr:
        parts = votes.strip().split()
        srnm, votes = parts[0], int(parts[1])
        ht.insert(srnm, int(votes))
    return ht.get_results()

if __name__ == '__main__':
    #elections_generator()
    with open('input.txt') as f:
        lines = f.readlines()
    res = elections(lines)
    with open('output.txt', 'w') as f:
        for r in res:
            f.write(f'{r[0]} {r[1]}\n')
    print(res)