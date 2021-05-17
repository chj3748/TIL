# 문자열 정규표현식 | bj 9342 염색체
import sys
# import itertools
# from math import factorial
# from collections import deque
# import heapq
# from collections import defaultdict
# import math
import re

# sys.setrecursionlimit(int(1e9))

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
# 문자열은 {A, B, C, D, E, F} 중 0개 또는 1개로 시작해야 한다.
# 그 다음에는 A가 하나 또는 그 이상 있어야 한다.
# 그 다음에는 F가 하나 또는 그 이상 있어야 한다.
# 그 다음에는 C가 하나 또는 그 이상 있어야 한다.
# 그 다음에는 {A, B, C, D, E, F} 중 0개 또는 1개가 있으며, 더 이상의 문자는 없어야 한다.
p = re.compile('^[A-F]?[A]+[F]+[C]+[A-F]?$')
for _ in range(N):
    string = input()
    if p.match(string):
        print('Infected!')
    else:
        print('Good')
