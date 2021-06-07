# dp 배낭문제 | bj 12865 평범한 배낭
# (knapsack)배낭문제 기본
import sys


def input():
    return sys.stdin.readline().rstrip()


N, K = map(int, input().split())
# [무게, 가치]
somethings = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(K + 1) for _ in range(N + 1)]
answer = 0
for i in range(1, N + 1):
    w, v = somethings[i - 1]
    for j in range(K + 1):
        if w <= j:
            dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w])
        else:
            dp[i][j] = dp[i - 1][j]
        if answer < dp[i][j]:
            answer = dp[i][j]

print(answer)