# 문자열 | bj 17609 회문
# http://boj.kr/35708a61bb1d4149952929e8154ba152
import sys
# import itertools
# from math import factorial
# from collections import deque
# import heapq
# from collections import defaultdict
# import math

# sys.setrecursionlimit(int(1e9))

def input():
    return sys.stdin.readline().rstrip()


def palin(start, end, del_cnt):
    if del_cnt == 2:  # 아무것도 아님
        return del_cnt
    while start <= end:
        if string[start] != string[end]:  # 유사 팰린드롬
            a = palin(start + 1, end, del_cnt + 1)
            b = palin(start, end - 1, del_cnt + 1)
            return a if a <= b else b
        start += 1
        end -= 1
    else:  # 팰린드롬
        return del_cnt


for T in range(int(input())):
    string = input()
    print(palin(0, len(string) - 1, 0))
