# dp | programmers 스티커 모으기(2)
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(sticker):
    n = len(sticker)
    # [0번 인덱스 사용, 사용 x]
    dp = [[0, 0] for _ in range(n)]
    dp[0] = [sticker[0], 0]
    if n == 1:
        return max(dp[0])

    dp[1] = [sticker[0], sticker[1]]

    for i in range(2, n):
        if i != n - 1:
            dp[i][0] = max(dp[i - 1][0], dp[i - 2][0] + sticker[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 2][1] + sticker[i])

    max_val = 0
    for val1, val2 in dp:
        if max_val < val1:
            max_val = val1

        if max_val < val2:
            max_val = val2

    return max_val