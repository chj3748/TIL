# swea 5188 최소합
def b_f(i, j, total, n):
    global min_sum
    if i == n - 1 and j == n - 1:
        min_sum=min(min_sum,total)
        return
    if i + 1 < n:
        b_f(i + 1, j, total + board[i + 1][j], n)
    if j + 1 < n:
        b_f(i, j + 1, total + board[i][j + 1], n)


for t in range(1,int(input())+1):
    n = int(input())
    board = [ list(map(int,input().split())) for _ in range(n) ]
    global min_sum
    min_sum= 2600

    b_f(0,0,board[0][0],n)

    print('#{} {}'.format(t, min_sum))