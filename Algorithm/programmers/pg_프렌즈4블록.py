# 구현 | programmers 프렌즈4블록
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(m, n, board):
    from collections import deque
    answer = 0
    board = [deque(row) for row in zip(*board[::-1])]

    def find_22():
        del_list = []
        for i in range(n - 1):
            for j in range(m - 1):
                val1 = board[i][j]
                if not val1:
                    continue
                val2 = board[i + 1][j]
                val3 = board[i][j + 1]
                val4 = board[i + 1][j + 1]
                if val1 == val2 == val3 == val4:
                    del_list += [[i, j], [i + 1, j], [i, j + 1], [i + 1, j + 1]]
        return del_list

    def delete_22(del_list):
        cnt = 0
        for ele in del_list:
            x, y = ele
            if not board[x][y]:
                continue
            board[x][y] = 0
            cnt += 1
        return cnt

    def fall_22():
        for idx, row in enumerate(board):
            temp = deque([ele for ele in row if ele != 0])
            for _ in range(m - len(temp)):
                temp.append(0)
            board[idx] = temp

    while True:
        del_list = find_22()
        if not del_list:
            break
        cnt = delete_22(del_list)
        answer += cnt
        fall_22()
    return answer