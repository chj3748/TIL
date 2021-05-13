# dfs bfs 그래프 | bj 14716 현수막
import sys


# import itertools
# from math import factorial
# from collections import deque
# import heapq
# import math

# sys.setrecursionlimit(int(1e9))
def input():
    return sys.stdin.readline().rstrip()


M, N = map(int, input().split())
banner = [list(map(int, input().split())) for _ in range(M)]


def find_string(row, col):
    stack = [(row, col)]
    banner[row][col] = 0
    while stack:
        x, y = stack.pop()
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N:
                if banner[nx][ny]:
                    stack.append((nx, ny))
                    banner[nx][ny] = 0
    return 1


string_cnt = 0
for i in range(M):
    for j in range(N):
        if banner[i][j]:
            string_cnt += find_string(i, j)

print(string_cnt)
