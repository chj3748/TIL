# dfs 분리집합 | bj 16724 피리 부는 사나이
# github.com/chj3748
# 유니온-파인드를 생각하면 간단한 문제
# 혹은 사이클이 발생했을때가 하나의 세이프존이라는 것을 캐치했다면 금방 품
import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
dm = defaultdict(int)
dm['U'] = [-1, 0]
dm['D'] = [1, 0]
dm['L'] = [0, -1]
dm['R'] = [0, 1]
maps = [list(input()) for _ in range(N)]


def move_dir(row, col, number):
    stack = [[row, col]]
    while stack:
        x, y = stack.pop()
        d = dm[maps[x][y]]  # 움직일 방향
        maps[x][y] = number
        nx, ny = x + d[0], y + d[1]
        if dm[maps[nx][ny]]:
            stack.append([nx, ny])
        # 현재 숫자보다 낮은 칸을 만났다면, 싸이클이 있는 그룹에 포함이라는 것
        elif maps[nx][ny] < number:
            return 0
    return 1


safe_zone = 0
num = 0
for r in range(N):
    for c in range(M):
        if dm[maps[r][c]]:
            num += 1
            safe_zone += move_dir(r, c, num)
print(safe_zone)
