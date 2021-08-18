# dp | bj 14925 목장 건설하기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


M, N = map(int, input().split())
ranch = [list(map(int, input().split())) for _ in range(M)]

dp = [[0] * N for _ in range(M)]

max_area = 0

for r in range(M):
    for c in range(N):
        if ranch[r][c]:
            continue
        if r == 0 or c == 0:
            dp[r][c] = 1
        else:
            dp[r][c] = 1 + min(dp[r - 1][c - 1], dp[r - 1][c], dp[r][c - 1])
        if max_area < dp[r][c]:
            max_area = dp[r][c]

print(max_area)