# 해시 구현 파싱 | baekjoon 19583 싸이버개강총회
# github.com/chj3748
import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


time_s, time_e, time_se = input().split()
checked = defaultdict(int)
cnt = 0
while True:
    temp = input()
    if not temp:
        break
    t, name = temp.split()

    if t <= time_s:
        checked[name] = t
    elif time_e <= t <= time_se:
        if not checked[name]:
            continue
        cnt += 1
        checked[name] = 0
print(cnt)
