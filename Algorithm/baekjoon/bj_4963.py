# 그래프 탐색 bfs dfs | bj 4963 섬의 개수
import sys
import collections

inp = sys.stdin.readline

dm = [
    [0, 1],
    [1, 0],
    [-1, 0],
    [0, -1],
    [1, 1],
    [1, -1],
    [-1, 1],
    [-1, -1]
]

while True:
    w, h = map(int, inp().split())
    if w == 0 and h == 0:
        break
    # 0으로 둘러싼 지도 생성
    maps = [[0] * (w + 2)] + [[0] + list(map(int, inp().split())) + [0] for _ in range(h)] + [[0] * (w + 2)]

    island = 0

    # 각 지점별로 육지인지 바다인지 체크
    for row in range(1, h + 1):
        for col in range(1, w + 1):
            if maps[row][col] == 1:
                island += 1
                maps[row][col] = 0
                q = collections.deque()
                q.append([row, col])
                # 만약 육지면 연결된 모든 육지를 찾아서 0으로 바꿈
                while q:
                    y, x = q.popleft()
                    for d in dm:
                        nx, ny = x + d[0], y + d[1]
                        if maps[ny][nx] == 1:
                            maps[ny][nx] = 0
                            q.append([ny, nx])
    print(island)
