# dp | programmers 등굣길
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(m, n, puddles):
    ways = [[0] * (n + 1) for _ in range(m + 1)]
    ways[1][1] = 1
    for px, py in puddles:
        ways[px][py] = -1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if ways[i][j] < 0:
                continue
            ways[i][j] += (ways[i - 1][j] if ways[i - 1][j] > -1 else 0) + (ways[i][j - 1] if ways[i][j - 1] > -1 else 0)
            ways[i][j] %= 1000000007
    return ways[m][n]