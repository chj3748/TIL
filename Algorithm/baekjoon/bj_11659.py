# 누적합 투포인터 | bj 11659 구간 합 구하기 4
import sys

# import itertools
# from math import factorial
# from collections import deque
# import heapq

# sys.setrecursionlimit(int(1e9))
inp = sys.stdin.readline

N, M = map(int, inp().split())
ac_sum = [0]  # 누적합 리스트  ac_sum[a]는 a번째 까지의 합을 나타냄
for val in map(int, inp().split()):
    ac_sum.append(ac_sum[-1] + val)

for _ in range(M):
    i, j = map(int, inp().split())
    # 따라서 i부터 j번째 까지의 합은 j번째 까지의 합에서 i바로 전까지의 합을 빼면 된다
    print( ac_sum[j] - ac_sum[i - 1])