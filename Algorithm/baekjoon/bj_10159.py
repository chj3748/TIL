# 위상정렬? 플로이드와샬 dfs bfs | bj 10159 저울
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
b_u = [[0]*(N + 1) for _ in range(N + 1)]
t_d = [[0]*(N + 1) for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    b_u[s][e] = 1
    t_d[e][s] = 1

def find_cnt(idx):
    cnt = N - 1
    visited = [0]*(N + 1)
    visited[idx] = 1
    deq = deque([idx])
    while deq:
        x = deq.pop()
        for i in range(N + 1):
            if b_u[x][i] == 1:
                if visited[i] == 0:
                    cnt -= 1
                    visited[i] = 1
                    deq.append(i)

    deq = deque([idx])
    while deq:
        x = deq.pop()
        for i in range(N + 1):
            if t_d[x][i] == 1:
                if visited[i] == 0:
                    cnt -= 1
                    visited[i] = 1
                    deq.append(i)
    return cnt


for obj in range(1, N + 1):
    answer = find_cnt(obj)
    print(answer)
