# 누적합 | programmers 정수 삼각형
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(triangle):
    n = len(triangle)
    acc_sums = [[0] * n for _ in range(n)]
    acc_sums[0][0] = triangle[0][0]
    for i in range(1, n):
        for j in range(0, i + 1):
            if j in [0, i]:
                col = 0 if j == 0 else j - 1
                acc_sums[i][j] = triangle[i][j] + acc_sums[i - 1][col]
            else:
                acc_sums[i][j] = triangle[i][j] + max(acc_sums[i - 1][j - 1], acc_sums[i - 1][j])
    return max(acc_sums[n - 1])