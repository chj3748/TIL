# 백트래킹 재귀 | programmers N-Queen
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(n):
    answer = 0

    def nqueen(row, used):
        nonlocal answer
        if row == n:
            answer += 1
            return
        for col in range(n):
            for used_x, used_y in used:
                diff_x, diff_y = used_x - row, used_y - col
                if diff_y == 0:
                    break
                gradient = diff_x / diff_y
                if gradient in [1, -1]:
                    break
            else:
                nqueen(row + 1, used + [[row, col]])

    nqueen(0, [])
    return answer