# dp | bj 2294 동전2
import sys
sys.setrecursionlimit(10000)
inp = sys.stdin.readline

n, k = map(int, inp().split())
coins = set()
for _ in range(n):
    coins.add(int(inp()))
# coins.sort(reverse=True)
coins = list(coins)
coins.sort()
#  2 5 13 -> 15
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# 0 - 1 - 2 - 3 - 4 - 5  -  6  -  7  -
# 0 - 1 - 2 1 - 2 - 3 2  -  3  -  4  3
# 0 - 1 - 2 1 - 2 - 3 2  -  3  1  4  2

# min_coin_cnt = 100000
# possible = False
# def countCoin(total, cnt):
#     global min_coin_cnt
#     global possible
#     if total == k:
#         if min_coin_cnt> cnt:
#             min_coin_cnt = cnt
#         if not possible:
#             possible = True
#         return
#     if total > k:
#         return
#     for coin in coins:
#         if coin <= k:
#             countCoin(total + coin, cnt + 1)
#
# countCoin(0,0)
# if possible:
#     print(min_coin_cnt)
# else:
#     print(-1)

dp =[-1]*(k+1)
dp[0] = 0
for coin in coins :
    for possible_k in range(1, k+1):
        # 사용하는 동전이 만드려는 금액보다 크면 다음 금액으로
        if possible_k - coin < 0:
            continue
        # 만드려는 금액에서 사용금액을 뺀 나머지가 dp에 존재하지 않으면 다음 금액으로
        if dp[possible_k - coin] == -1:
            continue
        # 만드려는 금액이 현재 동전 포함으로 가능하며,
        # 값이 존재하지 않거나 더 작은 개수로 만들 수 있다면 값 변경
        if dp[possible_k] == -1 or dp[possible_k] > dp[possible_k - coin] + 1:
            # print(coin, possible_k)
            dp[possible_k] = dp[possible_k - coin] + 1
# print(dp)
print(dp[k])
