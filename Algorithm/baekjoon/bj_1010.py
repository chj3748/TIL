# 수학 조합 dp | bj 1010 다리 놓기
import sys

# import itertools
from math import factorial
from collections import deque

# sys.setrecursionlimit(int(1e9))
inp = sys.stdin.readline
T = int(inp())
dp = [[0] * 31 for _ in range(31)]
for i in range(31):
    for j in range(31):
        if i <= j:
            if i == 0:
                dp[i][j] = 1
            elif i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

for t in range(T):
    N, M = map(int, inp().split())
    print(dp[N][M])

# 다른 풀이
# factorial = [1]*30
# for i in range(1, 30):
#     factorial[i] = factorial[i-1]*i
#
# for _ in range(T):
#     N, M = map(int, input().split())
#     print(factorial[M] // (factorial[N]*factorial[M-N]))