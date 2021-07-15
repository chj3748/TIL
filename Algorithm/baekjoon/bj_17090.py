# dfs 분리집합 | bj 17090 미로 탈출하기
# github.com/chj3748
# 피리 부는 사나이와 비슷한 문제
import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


dm = defaultdict(int)
dm['D'] = [1, 0]
dm['R'] = [0, 1]
dm['U'] = [-1, 0]
dm['L'] = [0, -1]

N, M = map(int, input().split())
maps = [list(input()) for _ in range(N)]


def is_escape(row, col, tn):
    temp_cnt = 0
    stack = [[row, col]]
    escape = False
    while stack:
        x, y = stack.pop()
        temp_cnt += 1
        d = dm[maps[x][y]]
        maps[x][y] = tn
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < N and 0 <= ny < M:
            val = maps[nx][ny]
            if dm[val]:
                stack.append([nx, ny])
            else:
                if escape_num[val]:
                    escape = True
        else:
            escape = True
    if escape:
        return temp_cnt
    else:
        return 0



total = 0
try_num = 0
escape_num = defaultdict(int)
for r in range(N):
    for c in range(M):
        if dm[maps[r][c]]:
            result = is_escape(r, c, try_num)
            if result:
                total += result
                escape_num[try_num] = 1
            try_num += 1
print(total)