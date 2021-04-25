# 투포인터 | bj 2003 수들의 합2
import sys

# sys.setrecursionlimit(10 ** 9)
inp = sys.stdin.readline

N, M = map(int, inp().split())
num_arr = list(map(int, input().split()))
start = 0
end = 0
temp = 0
cnt = 0
while start <= end <= N:
    if temp > M:
        temp -= num_arr[start]
        start += 1
    elif temp <= M:
        if temp == M:
            cnt += 1
        if end < N:
            temp += num_arr[end]
            end += 1
        else:
            break

print(cnt)
