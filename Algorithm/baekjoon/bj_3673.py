# 누적합 | bj 3673 나눌 수 있는 부분 수열
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


c = int(input())
for _ in range(c):
    d, n = map(int, input().split())
    nums = list(map(int, input().split()))
    acc_sum = 0
    mod_cnt = [0] * d
    for i in range(n):
        acc_sum += nums[i]
        mod_cnt[acc_sum % d] += 1
    cnt = mod_cnt[0]
    for i in range(d):
        cnt += (mod_cnt[i] * (mod_cnt[i] - 1)) // 2
    print(cnt)
