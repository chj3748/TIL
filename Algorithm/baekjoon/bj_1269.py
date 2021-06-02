# 해시맵 | bj 1269 대칭 차집합
import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()


len_a, len_b = map(int, input().split())

dict_a = defaultdict(int)
for number in map(int, input().split()):
    dict_a[number] = 1
cnt = 0
for number in map(int, input().split()):
    if dict_a[number]:
        cnt += 1
answer = len_a - cnt + len_b - cnt
print(answer)
