# 이진탐색 | bj 13702 이상한 술집
import sys

def input():
    return sys.stdin.readline().rstrip()


N, K = map(int, input().split())
liters = []
max_liter = 0
for _ in range(N):
    liter = int(input())
    if max_liter < liter:
        max_liter = liter
    liters.append(liter)


def bin_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in range(N):
            cnt += liters[i] // mid
        if cnt >= K:
            start = mid + 1
        else:
            end = mid - 1
    return end


answer = bin_search(1, max_liter)
print(answer)
