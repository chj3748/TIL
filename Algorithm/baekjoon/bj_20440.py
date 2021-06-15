# 누적합 | bj 20440 니가 싫어 싫어 너무 싫어 싫어 오지마 내게 찝쩍대지마
import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
timeline = defaultdict(int)
for _ in range(N):
    start, end = map(int, input().split())
    timeline[start] += 1
    timeline[end] -= 1

max_cnt = 0
begin = -1
finish = -1
temp = 0
checking = False
for idx in sorted(timeline.keys()):
    cnt = timeline[idx]
    temp += cnt
    if max_cnt < temp:
        max_cnt = temp
        begin = idx
        checking = True
    elif checking:
        if max_cnt > temp:
            finish = idx
            checking = False

print(max_cnt)
print(begin, finish)

