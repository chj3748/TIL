# 수학 구현 | bj 2753 윤년
import sys
# import itertools
# from math import factorial
# from collections import deque
# import heapq
# import math

# sys.setrecursionlimit(int(1e9))

def input():
    return sys.stdin.readline().rstrip()


year = int(input())

print(1) if not year % 4 and (year % 100 or not year % 400) else print(0)
