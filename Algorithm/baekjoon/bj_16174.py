# 그래프 완전탐색 bfs | bj 16174 점프왕 쩰리 (Large)
import sys

# import itertools
# from math import factorial
from collections import deque


# import heapq
# import math

# sys.setrecursionlimit(int(1e9))
def input():
    return sys.stdin.readline().rstrip()


# 정사각형 내부에서만 움직이고, 아웃시 추락으로 패배
# 출발점은 0,0
# 이동가능 방향은 오른쪽과 아래 (왼쪽, 위 불가능)
# n,n 도착시 승리
# 한번에 이동할 수 있는 칸수 = 현재 밟고있는 칸에 쓰여진 수
# 승리 = 'HaruHaru' 패배 = 'Hing' 출력
N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
inf = float('inf')
q = deque()
q.append((0, 0))
while q:
    x, y = q.popleft()
    for dx, dy in ((0, 1), (1, 0)):
        nx, ny = x + dx * maps[x][y], y + dy * maps[x][y]
        if 0 <= nx < N and 0 <= ny < N:
            if nx == N - 1 and ny == N - 1:
                print('HaruHaru')
                sys.exit(0)
            q.append((nx, ny))
    maps[x][y] = inf
print('Hing')
