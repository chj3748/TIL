# 그래프 dfs bfs | bj 2146 다리 만들기
# github.com/chj3748
import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


N = int(input())

maps = [list(map(int, input().split())) for _ in range(N)]
answer = 200


def dfs(row, col, c):
    stack = [[row, col]]
    while stack:
        x, y = stack.pop()
        maps[x][y] = c
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if maps[nx][ny] == 1:
                    stack.append([nx, ny])


def make_bridge(row, col, min_val, sea_c):
    dq = deque([[row, col, 0]])
    c = maps[row][col]
    while dq:
        x, y, cnt = dq.popleft()
        if cnt >= min_val:
            continue
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if maps[nx][ny] == c or maps[nx][ny] == sea_c:
                    continue
                elif sea_c < maps[nx][ny] <= 0:
                    dq.append([nx, ny, cnt + 1])
                    maps[nx][ny] = sea_c
                else:
                    return cnt
    return 202


land_num = 2
sea_num = -1
for i in range(N):
    for j in range(N):
        if maps[i][j] > 0:
            if maps[i][j] == 1:
                dfs(i, j, land_num)
                land_num += 1
            answer = min(answer, make_bridge(i, j, answer, sea_num))
            sea_num -= 1

print(answer)

