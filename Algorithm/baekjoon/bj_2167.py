# 누적합 | bj 2167 2차원 배열의 합
# github.com/chj3748
import sys

def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
acc_sum = [[0] * (M + 1) for _ in range(N + 1)]
for r in range(1, N + 1):
    temp = list(map(int, input().split()))
    for c in range(1, M + 1):
        acc_sum[r][c] = temp[c - 1] + acc_sum[r - 1][c] + acc_sum[r][c - 1] - acc_sum[r - 1][c - 1]

for t in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    temp = acc_sum[x2][y2] - acc_sum[x1 - 1][y2] - acc_sum[x2][y1 - 1] + acc_sum[x1 - 1][y1 - 1]
    print(temp)