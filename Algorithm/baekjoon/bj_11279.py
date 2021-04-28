# 우선순위 큐 | bj 11279 최대 힙
import sys
import heapq

# sys.setrecursionlimit(10 ** 9)
inp = sys.stdin.readline

N = int(inp())
h = []
for _ in range(N):
    temp = int(inp())
    if temp == 0:
        if h:
            print(-heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h, -temp)

