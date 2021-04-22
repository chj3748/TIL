# bfs graph | bj 3055 탈출
import sys
from collections import deque

inp = sys.stdin.readline


# . = 비어있는곳  * = 물이 차있는곳  X = 돌  D = 비버굴  S = 고슴도치
def bfs(hq, wq):
    global min_time
    minute = 0
    while hq:
        minute += 1
        if minute >= min_time:
            return
        # 물 범람
        for _ in range(len(wq)):
            row, col = wq.popleft()
            # 물은 사방으로 범람 하는데 돌과 비버굴이 아닌곳으로만 확장
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < R and 0 <= nc < C:
                    if forest_map[nr][nc] not in ('X', 'D', '*'):
                        forest_map[nr][nc] = '*'
                        wq.append([nr, nc])
        # 고슴도치 이동
        for _ in range(len(hq)):
            r_data, c_data = hq.popleft()
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r_data + dr, c_data + dc
                if 0 <= nr < R and 0 <= nc < C:
                    if forest_map[nr][nc] == '.':
                        forest_map[nr][nc] = minute  # 왔던길 되돌아가는거 방지
                        hq.append([nr, nc])
                    elif forest_map[nr][nc] == 'D':
                        if min_time > minute:
                            min_time = minute
                        return


R, C = map(int, inp().split())
forest_map = []
hedgehog_q = deque()
water_q = deque()
for row in range(R):
    temp = []
    for col, map_data in enumerate(inp()):
        if map_data == 'S':
            hedgehog_q.append([row, col])
        elif map_data == '*':
            water_q.append([row, col])
        temp.append(map_data)
    forest_map.append(temp)

forest_map[hedgehog_q[0][0]][hedgehog_q[0][1]] = 0

min_time = float('inf')
bfs(hedgehog_q, water_q)
if min_time == float('inf'):
    print("KAKTUS")
else:
    print(min_time)
