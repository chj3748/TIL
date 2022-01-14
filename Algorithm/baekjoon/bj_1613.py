# 플로이드워셜 bfs dfs graph | 1613 역사
# github.com/chj3748
import sys
from collections import defaultdict, deque

def input():
    return sys.stdin.readline().rstrip()


n, k = map(int, input().split())
linked = [[] for _ in range(n + 1)]
rev_linked = [[] for _ in range(n + 1)]

orders = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    fir, sec = map(int, input().split())
    linked[fir].append(sec)
    rev_linked[sec].append(fir)


def bfs(start, direction):
    visited = defaultdict(int)
    visited[start] = 1
    dq = deque([start])
    while dq:
        x = dq.popleft()
        next_in = linked[x] if direction == -1 else rev_linked[x]
        for nx in next_in:
            if visited[nx]:
                continue
            dq.append(nx)
            visited[nx] = 1
            orders[start][nx] = direction


for i in range(1, n + 1):
    bfs(i, 1)
    bfs(i, -1)

s = int(input())
for _ in range(s):
    fir, sec = map(int, input().split())
    print(orders[fir][sec])
