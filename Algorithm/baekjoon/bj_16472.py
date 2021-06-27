# 이분탐색 투포인터 | bj 16472 고냥이
import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()


N = int(input())
string = input()
str_dict = defaultdict(lambda: -1)
length = 0
answer = 0
for idx, s in enumerate(string):
    str_dict[s] = idx
    if len(str_dict) > N:
        del_idx = 100001
        del_s = ''
        for d, last_idx in str_dict.items():
            if last_idx < del_idx:
                del_s = d
                del_idx = last_idx
        del str_dict[del_s]
        length = idx - del_idx
    else:
        length += 1
    if answer < length:
        answer = length

if answer < length:
    answer = length

print(answer)