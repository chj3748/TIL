# 그래프 dfs bfs | bj 13565 침투
import sys


def input():
    return sys.stdin.readline().rstrip()

# 세로 가로
M, N = map(int, input().split())
fiber = [list(map(int,input())) for _ in range(M)]

answer = 'NO'

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(s):
    fiber[0][s] = 1
    stack = [(0,s)]
    while stack:
        x, y = stack.pop()
        for d in zip(dx, dy):
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < M and 0 <= ny < N:
                if fiber[nx][ny] == 0:
                    fiber[nx][ny] = 1
                    stack.append((nx, ny))
                    if nx == M - 1:
                        return 1
    return 0

for i in range(N):
    if fiber[0][i] == 0:
        if dfs(i):
            answer = 'YES'
            break
print(answer)