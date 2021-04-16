# bj 완전탐색 | 1051 숫자 정사각형
def check(y, x):
    global result
    num = arr[y][x]
    row_list = []
    for row in range(x + 1, M):
        if arr[y][row] == num:
            row_list.append(row)
    if not row_list:
        return
    size = []
    for val in row_list:
        size.append(val - x)
    for val in size:
        if 0 <= y + val < N and arr[y + val][x] == num and arr[y + val][x + val] == num:
            if (val+1) ** 2 > result:
                result = (val+1) ** 2


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

result = 1
for i in range(N):
    for j in range(M):
        check(i, j)

print(result)