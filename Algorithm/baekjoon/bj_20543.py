# 그리디 | bj 20543 폭탄 던지는 태영이
# 시간나면 다시풀어보자
import sys


def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
univ = [list(map(lambda x: int(x) * -1, input().split())) for _ in range(N)]
bombs = [[0] * N for _ in range(N)]
h = M // 2

for r in range(h, N - h):
    for c in range(h, N - h):
        bombs[r][c] = univ[r - h][c - h]
        if 0 <= r - h - 1 < N:
            bombs[r][c] -= univ[r - h - 1][c - h]
        if 0 <= c - h - 1 < N:
            bombs[r][c] -= univ[r - h][c - h - 1]
        if 0 <= r - h - 1 < N and 0 <= c - h - 1 < N:
            bombs[r][c] += univ[r - h - 1][c - h - 1]

        if 0 <= r - M < N:
            bombs[r][c] += bombs[r - M][c]
        if 0 <= c - M < N:
            bombs[r][c] += bombs[r][c - M]
        if 0 <= r - M < N and 0 <= c - M < N:
            bombs[r][c] -= bombs[r - M][c - M]
for row in bombs:
    print(*row)
