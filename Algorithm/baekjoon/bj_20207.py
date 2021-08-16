# 구현 정렬? | bj 20207 달력
# github.com/chj3748

import sys


def input():
    return sys.stdin.readline().rstrip()


days = [0] * 367
N = int(input())

for _ in range(N):
    s, e = map(int, input().split())
    days[s] += 1
    days[e + 1] -= 1

answer = 0
max_schedule = 0  # 하루에 최대 스케쥴 수
schedule_days = 0  # 연속된 스케쥴 일정 수
temp_cnt = 0

for idx, day in enumerate(days):
    temp_cnt += day
    if temp_cnt == 0:
        answer += max_schedule * schedule_days
        max_schedule = 0
        schedule_days = 0
    else:
        if max_schedule < temp_cnt:
            max_schedule = temp_cnt
        schedule_days += 1
else:
    if schedule_days:
        answer += max_schedule * schedule_days

print(answer)