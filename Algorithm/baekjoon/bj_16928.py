# graph bfs | baekjoon 16928 뱀과 사다리 게임
# github.com/chj3748
import sys
from collections import defaultdict, deque


def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
ladder_snake = defaultdict(int)

for _ in range(N + M):
    s, e = map(int, input().split())
    ladder_snake[s] = e

visited = [float('inf')] * 101

dq = deque()
dq.append([0, 1])
while dq:
    throw_cnt, position = dq.popleft()
    if visited[position] > throw_cnt:
        visited[position] = throw_cnt
    else:
        continue
    for i in range(1, 7):
        next_position = position + i
        if next_position > 100:
            continue
        if ladder_snake[next_position]:
            next_position = ladder_snake[next_position]
        if next_position == 100:
            print(throw_cnt + 1)
            sys.exit(0)
        dq.append([throw_cnt + 1, next_position])