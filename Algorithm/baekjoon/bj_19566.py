# 누적합 | 19566 수열의 구간 평균
import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()


N, K = map(int, input().split())
numbers = list(map(int, input().split()))
dp = defaultdict(int)
sm = 0
answer = 0

for i in range(N):
    sm += numbers[i]
    temp = sm - K * (i + 1)
    answer += dp[temp]
    dp[temp] += 1
print(answer + dp[0])
