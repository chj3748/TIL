# 그래프 bfs dfs | bj 3187 양치기 꿍
# 3184랑 똑같음
import sys

def input():
    return sys.stdin.readline().rstrip()

R, C = map(int, input().split())
back_yard = [list(input()) for _ in range(R)]
# k 양 v 늑대 # 울타리 . 빈곳
sheep_cnt = 0
wolf_cnt = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def cnt(r, c):
    stack = [[r, c]]
    s_cnt = 0
    w_cnt = 0
    if back_yard[r][c] == 'k':
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
                    if back_yard[nx][ny] == 'k':
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