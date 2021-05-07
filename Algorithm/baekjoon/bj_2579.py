# dp | bj 2579 계단 오르기
import sys

# import itertools
# from math import factorial
# from collections import deque
# import heapq
# import math

# sys.setrecursionlimit(int(1e9))
inp = sys.stdin.readline

N = int(inp())
stairs = [0] + [int(inp()) for _ in range(N)]
# dp[i] = [다음턴에 영향 없는것, 다음턴에 영향있는것]
dp = [[0, 0] for _ in range(N + 1)]
for i in range(1, N + 1):
    temp1 = dp[i - 1][0]
    temp2 = 0
    if 0 <= i - 2 < N:
        temp2 = max(dp[i - 2][0], dp[i - 2][1])
    # 현재 계산에서 다음턴에 영향이 없으려면 2칸전 계단의 아무값이나 받아도됨
    dp[i][0] = temp2 + stairs[i]
    # 단 다음계산에서 사용할 수 있는 값이려면 이전칸에서 영향을 안주는 값을 받아야 함
    dp[i][1] = temp1 + stairs[i]

print(max(dp[N]))
