# dp | bj 10714 케이크 자르기 2
import sys

# import itertools
# from math import factorial
# from collections import deque
# import heapq
# import math

sys.setrecursionlimit(int(1e9))
inp = sys.stdin.readline

n = int(inp())
cakes = [int(inp()) for _ in range(n)]

max_cake = 0
dp = [[-1] * n for _ in range(n)]  # dp[left][right]는 left부터 right까지 가져갔을때의 joi의 최대값

# 다음 케이크 위치를 반환
def plus(x):
    return (x + 1) % n

# 이전 케이크 위치를 반환
def minus(x):
    return (x - 1) % n  # 파이썬 특성상 음수를 나누면 양수 나머지가 나옴. c도 같은 방법으로 알고있음
                        # (n + x - 1) % n 과 같은 결과

# ioi의 케이크 선택법
def ioi(left, right):
    if plus(right) == left:
        return 0
    if cakes[minus(left)] > cakes[plus(right)]:  # ioi가 더 큰것(왼쪽)을 가져가므로 left쪽으로 케이크 확장
        return joi(minus(left), right)
    return joi(left, plus(right))  # ioi가 오른쪽을 가져가므로 총 케이크는 오른쪽으로 확장

# joi의 케이크 선택법
def joi(left, right):
    if dp[left][right] != -1:  # dp가 계산된적있다면 계산된 값 반환
        return dp[left][right]
    if plus(right) == left:  # 남은게 없다면 리턴 0
        dp[left][right] = 0
        return 0
    # joi가 왼쪽 케이크를 선택 할 경우
    temp1 = cakes[minus(left)] + ioi(minus(left), right)
    # joi가 오른쪽 케이크를 선택 할 경우
    temp2 = cakes[plus(right)] + ioi(left, plus(right))
    dp[left][right] = temp1 if temp1 > temp2 else temp2
    return dp[left][right]

# joi부터 케이크 선택함
for i in range(n):
    max_cake = max(max_cake, cakes[i] + ioi(i, i))

print(max_cake)
