# graph bfs | baekjoon 2667 단지번호붙이기
# github.com/chj3748
import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
town = [list(input()) for _ in range(N)]
answer = []
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def bfs(r, c):
    dq = deque([(r, c)])
    cnt = 1
    town[r][c] = '0'
    while dq:
        x, y = dq.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if town[nx][ny] == '1':
                town[nx][ny] = '0'
                dq.append((nx, ny))
                cnt += 1
    return cnt


for i in range(N):
    for j in range(N):
        if town[i][j] == '1':
            answer.append(bfs(i, j))

answer.sort()
print(len(answer))
for ans in answer:
    print(ans)
