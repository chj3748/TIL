# 그래프 완전탐색 bfs | bj 15806 영우의 기숙사 청소
import sys
# import itertools
# from math import factorial
from collections import deque
# import heapq
# import math

# sys.setrecursionlimit(int(1e9))

def input():
    return sys.stdin.readline().rstrip()

# 1일동안 곰팡이는 8방향으로 증식
d = [
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2),
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1)
]
# 벽으로 막혀있다면 x
# 청소를 해야하는지 안해도 되는지 'YES' 'NO'
# 방크기, 곰팡이 수, 검사하는 좌표 수, 남은 일 수
N, M, K, t = -1, -1, -1, -1
for inp in input().split():
    if inp.isdigit():
        if N != -1:
            if M != -1:
                if K != -1:
                    t = int(inp)
                else:
                    K = int(inp)
            else:
                M = int(inp)
        else:
            N = int(inp)

# [짝수시간 상태, 홀수시간 상태]
room = [[[0] * 2 for _ in range(N)] for _ in range(N)]
molds = deque()
for _ in range(M):
    row, col = -1, -1
    for inp in input().split():
        if inp.isdigit():
            if row != -1:
                col = int(inp)
            else:
                row = int(inp)
    room[row - 1][col - 1][0] = 1
    molds.append((row - 1, col - 1))

check_points = []
for _ in range(K):
    row, col = -1, -1
    for inp in input().split():
        if inp.isdigit():
            if row != -1:
                col = int(inp)
            else:
                row = int(inp)
    check_points.append((row - 1, col - 1))


def growing_molds(tt):
    l = len(molds)
    for _ in range(l):
        x, y = molds.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if room[nx][ny][tt % 2] != 1:
                    room[nx][ny][tt % 2] = 1
                    molds.append((nx, ny))


for tt in range(1, t + 1):
    growing_molds(tt)

for check_x, check_y in check_points:
    if room[check_x][check_y][t % 2] == 1:
        print('YES')
        break
else:
    print('NO')
