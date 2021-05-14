# 구현 bf | bj 4690 완전 세제곱
# http://boj.kr/fb355cbf95324465b430f4423567a2c4
import sys
# import itertools
# from math import factorial
# from collections import deque
# import heapq
# import math

# sys.setrecursionlimit(int(1e9))

def input():
    return sys.stdin.readline().rstrip()


# a, b, c, d > 0
for a in range(2, 100 + 1):
    for b in range(2, a):
        for c in range(b, a):
            for d in range(c, a):
                if a ** 3 == b ** 3 + c ** 3 + d ** 3:
                    print(f'Cube = {a}, Triple = ({b},{c},{d})')
