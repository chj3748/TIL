# 구현 분할정복 | baekjoon 17829 222-풀링
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
while len(arr) != 1:
    N = len(arr)
    temp = []
    for r in range(0, N, 2):
        row_result = []
        for c in range(0, N, 2):
            numbers = [arr[r][c], arr[r + 1][c], arr[r][c + 1], arr[r + 1][c + 1]]
            numbers.sort()
            row_result.append(numbers[-2])
        temp.append(row_result)
    arr = temp
print(arr[0][0])