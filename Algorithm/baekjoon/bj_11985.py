# dp | bj 11985 오렌지 출하
# http://boj.kr/f293bc24e6e347dba7b5aa08836171fe
import sys
# import itertools
# from math import factorial
# from collections import deque
# import heapq
# from collections import defaultdict
# import math

# sys.setrecursionlimit(int(1e9))

def input():
    return sys.stdin.readline().rstrip()


# 비용 최소 찾기
# 상자포장비용 + (가장 큰 오렌지 - 가장 작은 오렌지) * 담은 갯수
N, M, K = map(int, input().split())
oranges = []
inf = float('inf')
dp = [inf] * N
dp[0] = K  # 한개를 포장하면 비용은 K
for idx in range(N):
    oranges.append(int(input()))
    if idx > 0:
        max_size = oranges[idx]
        min_size = oranges[idx]
        for j in range(M):  # idx번째 오렌지를 포함해서 최대 M개의 오렌지를 그룹화
            left_idx = idx - j  # 그룹에서 제일 왼쪽 인덱스
            if left_idx >= 0:  # 제일 왼쪽 인덱스가 음수면 x
                if max_size < oranges[left_idx]:  # 최대값 최소값 갱신
                    max_size = oranges[left_idx]
                if min_size > oranges[left_idx]:
                    min_size = oranges[left_idx]
                if left_idx - 1 >= 0:  # 그룹화 갯수, 최소 둘 이상의 그룹으로 쪼개질 경우
                    temp = dp[left_idx - 1] + K + (max_size - min_size) * (j + 1)
                else:  # 첫 그룹에 다 담을 수 있고, 다 담는 경우
                    temp = K + (max_size - min_size) * (j + 1)
                if dp[idx] > temp:
                    dp[idx] = temp
print(dp[N - 1])
