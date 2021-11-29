# 구현 | programmers 행렬 테두리 회전하기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(rows, columns, queries):
    answer = []
    arr = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    for query in queries:
        x1, y1, x2, y2 = map(lambda x: x - 1, query)
        min_val = arr[x1 + 1][y1]
        temp = min_val
        total_cnt = (x2 - x1 + y2 - y1) * 2
        nx, ny = x1, y1
        d = [0, 1]
        for i in range(total_cnt):
            if i == y2 - y1:
                d = [1, 0]
            elif i == x2 - x1 + y2 - y1:
                d = [0, -1]
            elif i == x2 - x1 + 2 * (y2 - y1):
                d = [-1, 0]
            next_val = arr[nx][ny]
            arr[nx][ny] = temp
            temp = next_val
            nx, ny = nx + d[0], ny + d[1]
            if min_val > temp:
                min_val = temp
        else:
            arr[x1][y1] = temp
        answer.append(min_val)

    return answer