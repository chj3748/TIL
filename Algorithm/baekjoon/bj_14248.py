# bfs 그래프 | bj 14248 점프 점프
import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
stepstones = list(map(int, input().split()))
s = int(input()) - 1
visited = [0] * n
q = deque([s])
visited[s] = 1
answer = 1
while q:
    idx = q.popleft()
    jump = stepstones[idx]
    for dx in (1,-1):
        nx = idx + dx * jump
        if 0 <= nx < n:
            if not visited[nx]:
                q.append(nx)
                visited[nx] = 1
                answer += 1
print(answer)
