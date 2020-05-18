# 스티커 붙이기
def turn90(arr): # 시계방향 회전
    arr90= list(zip(*arr[::-1]))
    return arr90


def check(x, y, sticker_array):
    r, c = len(sticker_array), len(sticker_array[0])
    for i in range(r):
        for j in range(c):
            if sticker_array[i][j] == 0:
                continue
            elif notebook[x + i][y + j] == 1:
                return False  # 겹치는 부분 있음
    return True  # 스티커 붙일 수 있다.


# laptop에 스티커를 붙인다.
def attach(x, y, sticker_array):
    r, c = len(sticker_array), len(sticker_array[0])
    for i in range(r):
        for j in range(c):
            if sticker_array[i][j] == 1:
                notebook[x + i][y + j] = 1


if __name__ == '__main__':
    n, m, k = map(int, input().split())  # 세로(n), 가로(m), 스티커개수(k)
    notebook = [[0] * m for _ in range(n)]
    sticker = [{} for _ in range(k)]

    for i in range(k):
        sticker[i]['r'], sticker[i]['c'] = map(int, input().split())
        sticker[i]['board'] = [list(map(int, input().split())) for _ in range(sticker[i]['r'])]

    for num in range(k):
        cnt = 0  # 회전한 횟수. 3번보다 더 많이 회전할 순 없다.
        r, c = sticker[num]['r'], sticker[num]['c']
        board = sticker[num]['board']
        while cnt < 4:
            if r > n or c > m:  # 크기 비교
                r, c, board = c, r, turn90(board)
                cnt += 1
                continue
            success = 0
            for i in range(0, n - r + 1):
                for j in range(0, m - c + 1):
                    if not check(i, j, board): continue
                    ## 스티커를 붙일 수 있다면?
                    attach(i, j, board)
                    success = 1
                    break
                if success: break
            if success:
                break
            else:
                r, c, board = c, r, turn90(board)
                cnt += 1

    anv = 0
    for i in range(n):
        for j in range(m):
            if notebook[i][j] == 1: anv += 1
    print(anv)


