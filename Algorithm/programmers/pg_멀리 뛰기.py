# dp | programmers 멀리 뛰기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567
    return dp[n]