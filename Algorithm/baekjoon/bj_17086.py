# bfs 그래프 | bj 17086 아기 상어 2
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]
sharks = []
for i in range(N):
    for j in range(M):
        if sea[i][j]:
            sharks.append([i, j])


def bfs(r, c):
    result = 50
    for shark in sharks:
        dist = max(abs(r - shark[0]), abs(c - shark[1]))
        if result > dist:
            result = dist
    return result


answer = 0
for i in range(N):
    for j in range(M):
        if sea[i][j]:
            continue
        temp = bfs(i, j)
        if answer < temp:
            answer = temp

print(answer)
