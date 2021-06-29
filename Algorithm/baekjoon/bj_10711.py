# bfs 그래프 | 10711 모래성
import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


dm = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, 1], [1, -1]]

H, W = map(int, input().split())
sand_castle = [[int(val) if not val == '.' else 0 for val in input()] for _ in range(H)]
discounts = deque()
for i in range(H):
    for j in range(W):
        if not sand_castle[i][j]:
            discounts.append([i, j])


wave_cnt = 0
while discounts:
    l_discounts = len(discounts)
    change_cnt = 0
    for _ in range(l_discounts):
        x, y = discounts.popleft()
        for d in dm:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < H and 0 <= ny < W:
                if sand_castle[nx][ny]:
                    sand_castle[nx][ny] -= 1
                    if not sand_castle[nx][ny]:
                        change_cnt += 1
                        discounts.append([nx, ny])
    if change_cnt:
        wave_cnt += 1

else:
    print(wave_cnt)

