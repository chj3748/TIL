# dp | bj 14430 자원 캐기
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
dx = [1, 0]
dy = [0, 1]
for i in range(N):
    for j in range(M):
        if not i and not j:
            continue
        elif not i:
            maps[i][j] += maps[i][j - 1]
        elif not j:
            maps[i][j] += maps[i - 1][j]
        else:
            maps[i][j] += max(maps[i - 1][j], maps[i][j - 1])

print(maps[N - 1][M - 1])
