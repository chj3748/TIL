# dfs bfs 그래프 | bj 1926 그림
import sys


def input():
    return sys.stdin.readline().rstrip()


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
drawing = [list(map(int, input().split())) for _ in range(n)]


def check_drawing(x, y):
    stack = [[x, y]]
    drawing[x][y] = 0
    cnt = 1
    while stack:
        x, y = stack.pop()
        for d in zip(dx, dy):
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < m:
                if drawing[nx][ny]:
                    stack.append([nx, ny])
                    cnt += 1
                    drawing[nx][ny] = 0
    return cnt


answer = 0
drawing_cnt = 0
for i in range(n):
    for j in range(m):
        if drawing[i][j]:
            area = check_drawing(i, j)
            drawing_cnt += 1
            if answer < area:
                answer = area
print(drawing_cnt)
print(answer)
