# 누적합 | bj 20438 출석체크
import sys


def input():
    return sys.stdin.readline().rstrip()


N, K, Q, M = map(int, input().split())
sleeps = [0] * (N + 3)
attendance = [0] * (N + 3)
for sleep_student in map(int, input().split()):
    sleeps[sleep_student] = 1

for check in map(int, input().split()):
    if sleeps[check]:
        continue
    mul = 1
    while True:
        if not sleeps[check * mul]:
            attendance[check * mul] = 1
        mul += 1
        if check * mul > N + 2:
            break
acc_sum = [0] * (N + 3)
for i in range(3, N + 3):
    acc_sum[i] = acc_sum[i - 1] + attendance[i]

for _ in range(M):
    a, b = map(int, input().split())
    print((b - a + 1) - (acc_sum[b] - acc_sum[a - 1]))