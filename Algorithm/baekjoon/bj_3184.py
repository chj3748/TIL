# 그래프 dfs bfs | bj 3184 양
import sys

def input():
    return sys.stdin.readline().rstrip()

R, C = map(int, input().split())
back_yard = [list(input()) for _ in range(R)]
# o 양 v 늑대 # 울타리 . 빈곳
sheep_cnt = 0
wolf_cnt = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def cnt(r, c):
    stack = [[r, c]]
    s_cnt = 0
    w_cnt = 0
    if back_yard[r][c] == 'o':
        s_cnt += 1
    elif back_yard[r][c] == 'v':
        w_cnt += 1
    back_yard[r][c] = '#'
    while stack:
        x, y = stack.pop()
        for d in zip(dx, dy):
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < R and 0 <= ny < C:
                if back_yard[nx][ny] != '#':
                    stack.append([nx, ny])
                    if back_yard[nx][ny] == 'o':
                        s_cnt += 1
                    elif back_yard[nx][ny] == 'v':
                        w_cnt += 1
                    back_yard[nx][ny] = '#'
    if s_cnt > w_cnt:
        w_cnt = 0
    else:
        s_cnt = 0
    return s_cnt, w_cnt


for row in range(R):
    for col in range(C):
        if back_yard[row][col] != '#':
            temp = cnt(row, col)
            sheep_cnt += temp[0]
            wolf_cnt += temp[1]
print(sheep_cnt, wolf_cnt)
#
# # 요일은 0~ 6으로 표기
# # 시작날짜 start 끝날짜 end
# # 시작날짜 요일 w
# # 평일 = f
# def cal(start, end, w):
#     if w >= 5:
#         start += 7 - w
#         w = 0
#     diff = end - start + 1
#     m = 2 if diff % 7 + w >= 7 else (1 if (diff % 7 + w) % 7 == 6 else 0)
#     f = diff - (diff // 7) * 2 - m
#     return f
#
