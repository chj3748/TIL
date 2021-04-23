# 이분탐색 | bj 2805 나무 자르기
import sys

# sys.setrecursionlimit(10 ** 9)
inp = sys.stdin.readline

N, M = map(int, inp().split())
trees = list(map(int, inp().split()))
min_H = 0
max_H = max(trees)
height = 0
while min_H <= max_H:
    mid = (min_H + max_H) // 2
    temp = 0
    for tree in trees:
        get_m = tree - mid
        if get_m > 0:
            temp += get_m
            if temp >= M:
                break
    # print(temp, min_H, mid, max_H)
    if temp < M:  # 수확량이 적다 -> mid가 높게 있다 -> mid를 낮춰라
        max_H = mid - 1
    else:  # 수확량이 많다 -> 톱길이를 늘리자 => mid를 높여라
        min_H = mid + 1
        if height < mid:
            height = mid

print(height)
