# dp 누적합 | bj 11660 구간 합 구하기 5
import sys
input = sys.stdin.readline

# 1 시간초과
# N, M = map(int, input().split())
# maps = [ list(map(int,input().split())) for _ in range(N) ]

# for _ in range(M):
#     x1, y1, x2, y2 = map(int,input().split())
#     temp_sum = 0
#     for x in range(x1 - 1, x2):
#         temp_sum += sum(maps[x][y1 - 1:y2])
#     print(temp_sum)

# a1      a1a2    a1a2a3          a1a2a3a4
# a1a5 a1a2a5a6 a1a2a3a5a6a7 a1a2a3a4a5a6a7a8

N, M = map(int, input().split())
N += 1 # out of range 방지 0번 index 추가
# maps 및 dp 배열생성
arr = [0] * N
dp = [0] * N
for i in range(1, N):
    arr[i] = [0] + list(map(int, input().split()))
    dp[i] = [0] * N
arr[0] = dp[0] = [0] * N

# dp 배열 값 입력
for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = arr[i][j] + dp[i-1][j] + dp[i][j-1] -dp[i-1][j-1]
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    # 가장 큰 범위에서 구해야하는 바깥 범위 두곳을 빼주고 중복되어서 제거된 곳은 한번 더해 준다
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])