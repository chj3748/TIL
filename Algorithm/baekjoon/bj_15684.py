# bj dp bfs | 15684 사다리 조작
def check(maps):
    for col in range(1, len(maps[0]) - 2):
        start = col
        for row in range(len(maps)):
            if maps[row][col] == 1:
                col += 1
            elif maps[row][col - 1] == 1:
                col -= 1
        if col != start:
            return False
    return True


def add_ladder(maps, cnt, limit):
    if cnt == limit:
        if check(maps):
            return True
    else:
        for y in range(len(maps)):
            for x in range(1, len(maps[0]) - 2):
                if maps[y][x] != 1 and maps[y][x - 1] != 1 and maps[y][x + 1] != 1:
                    maps[y][x] = 1
                    if add_ladder(maps, cnt + 1, limit):
                        return True
                    maps[y][x] = 0


N, M, H = map(int, input().split())
ladder = [[0] * (N + 2) for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    ladder[a - 1][b] = 1

result = -1

for i in range(4):
    if add_ladder(ladder, 0, i):
        result = i
        break
print(result)
