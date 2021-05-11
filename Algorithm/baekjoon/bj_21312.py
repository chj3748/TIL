# 수학 구현 사칙연산 | bj 21312 홀짝 칵테일
import sys


# import itertools
# from math import factorial
# from collections import deque
# import heapq
# import math

# sys.setrecursionlimit(int(1e9))


def input():
    return sys.stdin.readline().rstrip()


odd_num = -1
even_num = -1
for number in map(int, input().split()):
    if number % 2:
        if odd_num == -1:
            odd_num = number
        else:
            odd_num *= number
    else:
        if even_num == -1:
            even_num = number
        else:
            even_num *= number
if odd_num != -1:
    print(odd_num)
else:
    print(even_num)
