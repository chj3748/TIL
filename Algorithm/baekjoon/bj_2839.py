# dp greedy | bj 2839 설탕 배달
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())

dp = [5001] * ((n + 1) if n > 4 else 6)
dp[3] = 1
dp[5] = 1
for i in range(6, n + 1):
    dp[i] = min(dp[i - 3], dp[i - 5]) + 1

print(-1 if dp[n] > 5000 else dp[n])
