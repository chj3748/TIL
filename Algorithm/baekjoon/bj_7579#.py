# 배낭문제(knapsack) dp | bj 7579 앱
import sys

# import itertools
# from math import factorial
# from collections import deque
# import heapq
# import math

# sys.setrecursionlimit(int(1e9))
inp = sys.stdin.readline

N, M = map(int, inp().split())
need_m = [0] + list(map(int, inp().split()))
cost = [0] + list(map(int, inp().split()))
# 최대 비용
sum_cost = sum(cost)
# 세로는 앱 수 많큼, 가로는 최대 비용만큼
# dp[i][j]는 총 비용 j중에 i번째 앱을 끄는 비용을 지불했을때 확보가능한 최대한의 메모리
dp = [[0] * (sum_cost + 1) for _ in range(N + 1)]
inf = int(1e9)
# 최소값을 찾아야하니까 초기값은 엄청 큰 수
answer = inf
# 1번 앱부터 해당 비용이 남았을때 끌지 말지 고민
for i in range(1, N + 1):
    for j in range(sum_cost + 1):
        if j < cost[i]:  # 앱의 비용이 가능한 비용보다 크면 끌 수 없다
            dp[i][j] = dp[i - 1][j]
        else:  # 앱의 비용이 가능한 비용보다 작으면 끄고 돈이 남은 만큼 메모리를 더 확보가능하다
            # 따라서 각 비용으로 얻을 수 있는 최대한의 메모리를 산출 할 수 있다.
            dp[i][j] = max(need_m[i] + dp[i - 1][j - cost[i]], dp[i - 1][j])
        # 각 자리 계산이 끝났을때 최대확보가능한 메모리가 요구치보다 높을경우
        # 최소 비용을 구한다
        if dp[i][j] >= M:
            if answer > j:
                answer = j

print(answer)
