# 구현 | 14499 주사위 굴리기
import sys


def input():
    return sys.stdin.readline().rstrip()


N, M, x, y, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
d = [
    [],
    [0, 1],
    [0, -1],
    [-1, 0],
    [1, 0]
]
dice = [0, 0, 0, 0, 0, 0]  # [위, 동, 서, 북, 남, 아래]
for order in map(int, input().split()):  # 동, 서, 북, 남
    nx, ny = x + d[order][0], y + d[order][1]
    if 0 <= nx < N and 0 <= ny < M:
        x, y = nx, ny
        if order == 1:
            dice = [dice[2], dice[0], dice[5], dice[3], dice[4], dice[1]]
        if order == 2:
            dice = [dice[1], dice[5], dice[0], dice[3], dice[4], dice[2]]
        if order == 3:
            dice = [dice[4], dice[1], dice[2], dice[0], dice[5], dice[3]]
        if order == 4:
            dice = [dice[3], dice[1], dice[2], dice[5], dice[0], dice[4]]
        if maps[x][y]:
            dice[5], maps[x][y] = maps[x][y], 0
        else:
            maps[x][y] = dice[5]

        print(dice[0])
    else:
        continue
