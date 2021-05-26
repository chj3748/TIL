# 누적합 | bj 10986 나머지 합
import sys


def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
acc_nums = [0] * (N + 1)
# 누적합의 나머지를 저장 할 배열
mods = [0]*M
for i in range(1, N + 1):
    acc_nums[i] = (acc_nums[i - 1] + numbers[i - 1]) % M
    mods[acc_nums[i]] += 1

answer = mods[0]
for i in range(M):
    if mods[i] > 1:
        # 나머지가 같은 구간끼리(정확히는 i+1~j 구간)는 M으로 나누어 떨어진다
        temp = (mods[i] * (mods[i] - 1)) // 2  # 나머지가 같은 구간을 뽑은 조합
        answer += temp

print(answer)
