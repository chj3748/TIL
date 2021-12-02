# graph bfs | programmers 게임 맵 최단거리
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(maps):
    from collections import deque
    dq = deque()
    dq.append([0, 0])
    n, m = len(maps), len(maps[0])
    for i in range(n):
        for j in range(m):
            maps[i][j] = 0 if maps[i][j] else -1
    maps[0][0] = 1
    while dq:
        x, y = dq.popleft()
        cnt = maps[x][y]
        for d in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + d[0], y + d[1]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if maps[nx][ny] == -1:
                continue
            if nx == n - 1 and ny == m - 1:
                return maps[x][y] + 1
            if not maps[nx][ny] or maps[nx][ny] > maps[x][y] + 1:
                dq.append([nx, ny])
                maps[nx][ny] = maps[x][y] + 1
    return -1