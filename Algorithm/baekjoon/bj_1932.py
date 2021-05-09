# dp | bj 1932 정수 삼각형
import sys

# import itertools
# from math import factorial
# from collections import deque
# import heapq
# import math

# sys.setrecursionlimit(int(1e9))
inp = sys.stdin.readline

n = int(inp())
pyramid = []
for _ in range(n):
    pyramid.append(list(map(int, inp().split())))
dp = [[0] * (i + 1) for i in range(n)]

for row in range(n):
    if row == 0:
        dp[0][0] = pyramid[0][0]
        continue
    for col in range(row + 1):
        if 0 < col < row: # 위에서 내려오는값이 두개인 경우
            dp[row][col] = pyramid[row][col] + max(dp[row - 1][col], dp[row - 1][col - 1])
        elif col == row: # 맨 오른쪽 위치 할 경우
            dp[row][col] = pyramid[row][col] + dp[row - 1][col - 1]
        else: # 맨 왼쪽 위치할 경우
            dp[row][col] = pyramid[row][col] + dp[row - 1][col]

print(max(dp[n - 1]))
