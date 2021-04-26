# dp 슬라이딩윈도우? | bj 2096 내려가기
import sys

# sys.setrecursionlimit(10 ** 9)
inp = sys.stdin.readline

N = int(inp())
# arr = [list() for _ in range(N)]

dp_min = [-1] * 3
dp_max = [-1] * 3

temp_dp_min = [0] * 3
temp_dp_max = [0] * 3
for row in range(N):
    for idx, col in enumerate(map(int, inp().split())):
        # 최대값 찾기 과정
        temp = []
        if 0 <= row - 1 < N:            # 뒤의 조건은 첫째줄일때 예외처리를 위한 조건
            if 0 <= idx - 1 < 3 and dp_max[idx - 1] != -1:
                temp.append(dp_max[idx - 1])
            if dp_max[idx] != -1:
                temp.append(dp_max[idx])
            if 0 <= idx + 1 < 3 and dp_max[idx + 1] != -1:
                temp.append(dp_max[idx + 1])
        if temp:
            temp_dp_max[idx] = col + max(temp)
        else:
            temp_dp_max[idx] = col
        # 최소값 찾기 과정
        temp = []
        if 0 <= row - 1 < N:
            if 0 <= idx - 1 < 3 and dp_min[idx - 1] != -1:
                temp.append(dp_min[idx - 1])
            if dp_min[idx] != -1:
                temp.append(dp_min[idx])
            if 0 <= idx + 1 < 3 and dp_min[idx + 1] != -1:
                temp.append(dp_min[idx + 1])
        if temp:
            temp_dp_min[idx] = col + min(temp)
        else:
            temp_dp_min[idx] = col
    dp_max = list(temp_dp_max)
    dp_min = list(temp_dp_min)

print(max(dp_max), min(dp_min))
