from measurments import *
from random_letters import *

def letters_sort(tuples):
   # sort in descending order by the number of letters' occurrences
    if len(tuples) > 1:
        sort_success = False
        n = len(tuples)
        while not sort_success:
            j = n - 1
            while j >= 0 and tuples[j - 1][1] >= tuples[j][1]:
                j -= 1
                if j > 0:
                    continue
                else:
                    sort_success = True
            while j > 0 and tuples[j - 1][1] < tuples[j][1]:
                tuples[j - 1], tuples[j] = tuples[j], tuples[j - 1]
                j -= 1

    sorted_vals = []
    for k, v in tuples:
        if v not in sorted_vals:
            sorted_vals.append(v)

    # find letters with equal number of occurences
    for v in sorted_vals:
        v_inds = []
        for i in range(len(tuples)):
            if tuples[i][1] == v:
                v_inds.append(i)
        # if found, sort in alphabetical order
        if len(v_inds) > 1:
            temp = tuples[v_inds[0]:v_inds[-1] + 1]
            n = len(temp)
            for i in range(1, n):
                j = i
                while j > 0 and temp[j][0] < temp[j - 1][0]:
                    temp[j - 1], temp[j] = temp[j], temp[j - 1]
                    j -= 1

            tuples[v_inds[0]:v_inds[-1] + 1] = temp

    return tuples

def create_palindrome(tuples):
    # check if any letters number of occurrences can make at least 1 pair
    if any([True if (v // 2) > 0 else False for k, v in tuples]):
        truth = [True if (v // 2) > 0 else False for k, v in tuples]
        true_inds = []
        for i in range(len(truth)):
            if truth[i]:
                true_inds.append(i)
        right_part = ''
        left_part = ''
        for k in true_inds:
            pairs = tuples[k][1] // 2
            left_part += tuples[k][0] * pairs
            right_part = tuples[k][0] * pairs + right_part
            tuples[k] = (tuples[k][0], tuples[k][1] - (pairs * 2))

        tuples = letters_sort(tuples)
        # check if any letters number of occurrences are non-zero
        if any([True if v > 0 else False for k, v in tuples]):
            truth = [True if v > 0 else False for k, v in tuples]
            true_inds = []
            for i in range(len(truth)):
                if truth[i]:
                    true_inds.append(i)
            # make in alphabetical order
            let_ind = true_inds[0]
            left_part += tuples[let_ind][0]

            return left_part + right_part
        return left_part + right_part
    return tuples[0][0]

@measure_memory_usage
@timeit
def plndrm():
    with open('input.txt') as f:
        data = f.readline()

    crazy_code = str(data)
    if len(crazy_code) < 2:
        return crazy_code

    tuples = []
    let_set = set()
    for i in crazy_code:
        if i not in let_set:
            tuples.append((i, 1))
            let_set.add(i)
        else:
            for l in range(len(tuples)):
                if tuples[l][0] == i:
                    num = tuples[l][1]
                    tuples[l] = (i, num + 1)

    sorted_tup = letters_sort(tuples)
    output = create_palindrome(sorted_tup)

    with open('output.txt', 'w') as f:
        f.writelines(output)

    return output

if __name__ == "__main__":
    abracadabra()
    palind = plndrm()
    print(palind)
    if len(palind) % 2 == 0:
        lft = palind[:len(palind)//2]
        rght = palind[len(palind)//2:]
        rght = rght[::-1]
        assert lft == rght, 'not a palindrome......'
    else:
        lft = palind[:len(palind) // 2]
        rght = palind[(len(palind) // 2) + 1:]
        rght = rght[::-1]
        assert lft == rght, 'not a palindrome......'