# 분할정복 재귀 | bj 1074 Z
import sys


def input():
    return sys.stdin.readline().rstrip()


N, r, c = map(int, input().split())
w = 2 ** N
total = 0
x1, x2 = 0, w - 1
y1, y2 = 0, w - 1
cell_cnt = (w ** 2) // 4
while True:
    x_mid = (x1 + x2) // 2
    y_mid = (y1 + y2) // 2
    if x1 >= x2 or y1 >= y2:
        break
    if r <= x_mid and c <= y_mid:  # 1번 위치
        x1, x2 = x1, x_mid
        y1, y2 = y1, y_mid
        total = total
    elif r <= x_mid and c > y_mid:  # 2번 위치
        x1, x2 = x1, x_mid
        y1, y2 = y_mid + 1, y2
        total += cell_cnt
    elif r > x_mid and c <= y_mid:  # 3번위치
        x1, x2 = x_mid + 1, x2
        y1, y2 = y1, y_mid
        total += cell_cnt * 2
    elif r > x_mid and c > y_mid:  # 4번 위치
        x1, x2 = x_mid + 1, x2
        y1, y2 = y_mid + 1, y2
        total += cell_cnt * 3
    cell_cnt //= 4
print(total)
