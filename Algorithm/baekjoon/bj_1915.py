# dp 누적합 | bj 1915 가장 큰 정사각형
import sys

# import itertools
# from math import factorial
# from collections import deque
# import heapq
# import math

# sys.setrecursionlimit(int(1e9))
inp = sys.stdin.readline

N, M = map(int, inp().split())
# arr 배열 자체를 dp배열처럼 수정하며 이용함
# arr[i][j] = arr[i][j]를 오른쪽 하단 꼭지점으로 하는 정사각형의 최대 크기
arr = [list(map(int, inp().strip())) for _ in range(N)]

answer = 0
for row in range(N):
    for col in range(M):
        if arr[row][col] == 1:
            # 정사각형이 확장되기 위해서는 왼쪽 상단으로 대각선에 사각형이 존재해야함
            if 0 <= row - 1 < N and 0 <= col - 1 < M:
                # 상단 왼쪽 대각선 중 최소값 만큼 모두 박스가 있을때 해당 최소값 만큼 확장가능
                # 즉 상단 3 왼쪽 2 대각선 5라면 현재 박스에서 3방향으로 최소 2개씩만큼은 확장이 가능함
                arr[row][col] += min(arr[row - 1][col - 1], arr[row - 1][col], arr[row][col - 1])
            # 최대 정사각형 크기 변경
            if answer < arr[row][col]:
                answer = arr[row][col]
print(answer ** 2)
