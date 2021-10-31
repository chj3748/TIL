# deque | programmers 삼각 달팽이
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(n):
    from collections import deque

    d = [[1, 0], [0, 1], [-1, -1]]
    dm = 0
    answer = []
    arr = [[0] * n for _ in range(n)]
    dq = deque()
    dq.append([0, 0])
    i = 1
    while dq:
        x, y = dq.popleft()
        arr[x][y] = i
        nx, ny = x + d[dm][0], y + d[dm][1]
        if not (0 <= nx < n and 0 <= ny < n) or arr[nx][ny]:
            dm = (dm + 1) % 3
            nx, ny = x + d[dm][0], y + d[dm][1]
        if (0 <= nx < n and 0 <= ny < n) and not arr[nx][ny]:
            dq.append([nx, ny])
        i += 1

    for i in range(n):
        for j in range(i + 1):
            answer.append(arr[i][j])
    return answer