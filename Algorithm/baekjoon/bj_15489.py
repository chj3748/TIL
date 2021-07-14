# 수학 dp | bj 15489 파스칼 삼각형
# github.com/chj3748
# dp로 어렵게 생각하다 오래걸린 문제
import sys


def input():
    return sys.stdin.readline().rstrip()


R, C , W = map(int, input().split())
dp = [[0] * 31 for _ in range(31)]
for r in range(31):
    for c in range(r + 1):
        if c == 0 or r == c:
            dp[r][c] = 1
        else:
            dp[r][c] = dp[r - 1][c - 1] + dp[r - 1][c]

R -= 1
C -= 1
answer = 0
for i in range(W):
    for j in range(i + 1):
        answer += dp[R + i][C + j]
print(answer)