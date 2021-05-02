# 조합 dp | bj 5569 출근 경로
import sys

# import itertools
# from math import factorial
# from collections import deque

# sys.setrecursionlimit(int(1e9))
inp = sys.stdin.readline

w, h = map(int, inp().split())
# dp의 첫인자가 0 => 1칸이동 1 => 2칸이동 즉, 1이면 방향전환이 가능하다는것
# dp의 두번째인자가 0 => 동으로 이동 1 => 북으로 이동
dp = [[[[0, 0] for _ in range(2)] for _ in range(101)] for _ in range(101)]

MOD = 100000

for row in range(2, h + 1):
    dp[row][1][0][0] = 1
for col in range(2, w + 1):
    dp[1][col][0][1] = 1

for row in range(2, h + 1):
    for col in range(2, w + 1):
        # 방향 전환이 불가능한 경우 = 첫번째 인자가 0인 경우
        # 이전칸에서 방향 전환을 한 경우이다
        dp[row][col][1][0] = dp[row - 1][col][0][1] % MOD
        dp[row][col][1][1] = dp[row][col - 1][0][0] % MOD
        # 방향전환이 가능한 경우는 = 첫번째 인자가 1인 경우
        # 이전칸에서 방향전환이 가능할때 + 불가능할때 이다
        dp[row][col][0][0] = (dp[row - 1][col][0][0] + dp[row - 1][col][1][0]) % MOD
        dp[row][col][0][1] = (dp[row][col - 1][0][1] + dp[row][col - 1][1][1]) % MOD

answer = 0
for i in range(2):
    for j in range(2):
        answer += dp[h][w][i][j]

print(answer%MOD)
