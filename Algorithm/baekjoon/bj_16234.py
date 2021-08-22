# 그래프 dfs bfs 시뮬레이션 | bj 16234 인구 이동
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


N, L, R = map(int, input().split())  # L보다 크거나 R보다 작으면 오픈
people = [list(map(int, input().split())) for _ in range(N)]
dm = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def checking(x, y):
    open_list = [[x, y]]
    stack = [[x, y, people[x][y]]]
    total = people[x][y]
    people[x][y] = -1
    while stack:
        r, c, val = stack.pop()
        for d in dm:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < N and 0 <= nc < N:
                if people[nr][nc] >= 0 and L <= abs(val - people[nr][nc]) <= R:
                    open_list.append([nr, nc])
                    stack.append([nr, nc, people[nr][nc]])
                    total += people[nr][nc]
                    people[nr][nc] = -1
    return total, open_list


def open_country():
    open_lists = []
    for i in range(N):
        for j in range(N):
            if people[i][j] >= 0:
                total_sum, open_list = checking(i, j)
                open_lists.append([total_sum, open_list])
    is_change = False
    for total, open_list in open_lists:
        val = total // len(open_list)
        if len(open_list) > 1:
            is_change = True
        for x, y in open_list:
            people[x][y] = val
    return is_change


t = 0
while True:
    sign = open_country()
    if sign:
        t += 1
    else:
        break

print(t)