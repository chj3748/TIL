# 문자열 | bj 9046 복호화
import sys
# import itertools
# from math import factorial
# from collections import deque
# import heapq
from collections import defaultdict
# import math

# sys.setrecursionlimit(int(1e9))

def input():
    return sys.stdin.readline().rstrip()


for T in range(int(input())):
    string = input()
    s_cnt = defaultdict(int)
    max_s = []
    max_cnt = 0
    for s in string:
        if s.isalpha():
            s_cnt[s] += 1
            if max_cnt < s_cnt[s]:
                max_cnt = s_cnt[s]
                max_s = [s]
            elif max_cnt == s_cnt[s]:
                max_s.append(s)
    if len(max_s) > 1:
        answer = '?'
    else:
        answer = max_s[0]
    print(answer)
