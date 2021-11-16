# dijkstra graph | programmers 배달
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(N, road, K):
    from collections import deque
    answer = 0
    dist = [K + 1] * (N + 1)
    arr = [[] for _ in range(N + 1)]

    for r in road:
        start, end, d = r
        arr[start].append([end, d])
        arr[end].append([start, d])

    dist[1] = 0
    dq = deque([1])
    while dq:
        x = dq.popleft()
        for nx, nd in arr[x]:
            if dist[x] + nd <= dist[nx]:
                dq.append(nx)
                dist[nx] = dist[x] + nd

    for d in dist:
        if d <= K:
            answer += 1

    return answer