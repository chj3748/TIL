# simulation | programmers 거리두기 확인하기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
dd = [[-1, 1], [1, 1], [1, -1], [-1, -1]]


def solution(places):
    answer = []

    def checking(x, y, rooms):
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < 5 and 0 <= ny < 5):
                continue
            if rooms[nx][ny] == 'P':
                return True
            elif rooms[nx][ny] == 'O':
                nnx, nny = nx + dx, ny + dy
                if not (0 <= nnx < 5 and 0 <= nny < 5):
                    continue
                if rooms[nnx][nny] == 'P':
                    return True
        return False

    def checking2(x, y, rooms):
        for i in range(4):
            dx, dy = dd[i]
            nx, ny = x + dx, y + dy
            if not (0 <= nx < 5 and 0 <= ny < 5):
                continue
            if rooms[nx][ny] == 'P':
                if not (rooms[x + dx][y] == 'X' and rooms[x][y + dy] == 'X'):
                    return True
        return False

    def find_p(rooms):
        for i in range(5):
            for j in range(5):
                if rooms[i][j] == 'P':
                    if checking(i, j, rooms):
                        return True
                    if checking2(i, j, rooms):
                        return True
        return False

    for place in places:
        if find_p(place):
            answer.append(0)
        else:
            answer.append(1)
    return answer
