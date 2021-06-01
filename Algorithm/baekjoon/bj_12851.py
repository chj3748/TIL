# 그래프 bfs | bj 12851 숨박꼭질 2
import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


N, K = map(int, input().split())
if K <= N:
    print(N - K)
    print(1)
    sys.exit(0)

status = [100001 for _ in range(100001)]
status[N] = 0
min_t = status[K]
cnt = 0

deq = deque()
deq.append([N, 0])
while deq:
    x, t = deq.popleft()
    if x == K:
        min_t = status[x]
        cnt += 1
    for nx in (x + 1, x - 1, x * 2):
        if 0 <= nx <= 100000:
            if status[nx] < t + 1:
                continue
            if min_t < t + 1:
                continue
            status[nx] = t + 1
            deq.append([nx, t + 1])
print(status[K])
print(cnt)
