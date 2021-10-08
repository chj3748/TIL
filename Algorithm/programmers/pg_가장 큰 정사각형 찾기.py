# dp | programmers 가장 큰 정사각형 찾기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(board):
    answer = 1 if 1 in board[0] else 0
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if not board[i][j]:
                continue
            board[i][j] += min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1])
            if board[i][j] >= answer:
                answer = board[i][j]
    return answer ** 2