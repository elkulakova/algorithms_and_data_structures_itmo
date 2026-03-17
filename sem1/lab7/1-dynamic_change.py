from generator import *
from measurments import *

@measure_performance
def dpchange(money, coins):
    mnc = [float('inf') for _ in range(0, money+1)]
    mnc[0] = 0
    for m in range(1, money+1):
        for i in range(len(coins)):
            if m >= coins[i]:
                mnc[m] = min(mnc[m], mnc[m - coins[i]] + 1)
    return mnc[money] if mnc[money] != float('inf') else -1

@measure_performance
def limited_dpchange(money, coins, lims):
    dp = [float('inf') for _ in range(0, money + 1)]
    dp[0] = 0
    for coin, cnt in zip(coins, lims):
        k = 1
        while cnt > 0:
            take = min(k, cnt)
            w = take * coin
            amount = take
            for x in range(money, w - 1, -1):
                dp[x] = min(dp[x], dp[x - w] + amount)
            cnt -= take
            k <<= 1

    if dp[money] == float('inf'):
        return -1
    return dp[money]

if __name__ == '__main__':
    cash_generator()
    with open('input.txt') as f:
        s, _ = map(int, f.readline().split())
        cs = list(map(int, f.readline().split()))
        lmts = list(map(int, f.readline().split()))
    res = dpchange(s, cs)
    res_limited = limited_dpchange(s, cs, lmts)
    with open('output.txt', 'w') as f:
        f.write(str(res))
    print(res, res_limited)