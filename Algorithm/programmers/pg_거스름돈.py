# greedy dp | programmers 거스름돈
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(n, money):
    dp = [0] * 100001
    dp[0] = 1
    for m in money:
        for i in range(m, n + 1):
            dp[i] += dp[i - m]
    return dp[n]