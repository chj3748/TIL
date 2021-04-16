# bj brute force | 2210 숫자판 점프
def brute_force(cnt, i, j, number):
    if cnt == 5:
        used.add(number)
        return
    else:
        for d in (0, 1), (1, 0), (-1, 0), (0, -1):
            ny, nx = i + d[0], j + d[1]
            if 0 <= ny < 5 and 0 <= nx < 5:
                brute_force(cnt + 1, ny, nx, number + num_board[ny][nx])


num_board = [input().split() for _ in range(5)]
used = set()
for i in range(5):
    for j in range(5):
        brute_force(0, i, j, num_board[i][j])
print(len(used))
