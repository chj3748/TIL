# dp | bj 2293 동전1
import sys
inp = sys.stdin.readline

n, k = map(int, inp().split())
coins = set()
for _ in range(n):
    coins.add(int(inp()))
# coins.sort(reverse=True)
coins = list(coins)
coins.sort()

dp = [0]*(k+1)
dp[0] = 1
for coin in coins:
    for make_money in range(1, k + 1):
        if coin <= make_money :
            if make_money - coin < 0:
                continue
            dp[make_money] += dp[make_money - coin]
print(dp[k])



