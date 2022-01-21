# graph bfs | baekjoon 7569 토마토
# github.com/chj3748
import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


N, M, H = map(int, input().split())
d = [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (-1, 0, 0), (1, 0, 0)]
ripe_tomato = deque()
unripe_tomato = 0
tomatos = []
for h in range(H):
    pannels = []
    for i in range(M):
        tomato = list(map(int, input().split()))
        for j in range(N):
            if tomato[j] == 1:
                ripe_tomato.append([h, i, j])
            elif tomato[j] == 0:
                unripe_tomato += 1
        pannels.append(tomato)
    tomatos.append(pannels)

if not unripe_tomato:
    print(0)
    sys.exit(0)


def possible(h, x, y):
    if not (0 <= h < H):
        return False
    if not (0 <= x < M):
        return False
    if not (0 <= y < N):
        return False
    return True


days = 0
while ripe_tomato:
    k = len(ripe_tomato)
    before_change = unripe_tomato
    for i in range(k):
        h, x, y = ripe_tomato.popleft()
        for dh, dx, dy in d:
            nh, nx, ny = h + dh, x + dx, y + dy
            if not possible(nh, nx, ny):
                continue
            if tomatos[nh][nx][ny] == 0:
                ripe_tomato.append([nh, nx, ny])
                tomatos[nh][nx][ny] = 1
                unripe_tomato -= 1
    if before_change != unripe_tomato:
        days += 1
    else:
        break

if unripe_tomato:
    print(-1)
else:
    print(days)
