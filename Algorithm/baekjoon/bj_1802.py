# 분할정복 문자열 | bj 1802 종이 접기
# http://boj.kr/28603d67d3014c79af724768c75865af
import sys
# import itertools
# from math import factorial
# from collections import deque
# import heapq
# import math

# sys.setrecursionlimit(int(1e9))

def input():
    return sys.stdin.readline().rstrip()

# 중앙을 기준으로 대칭이면 됨.
def origami(start, end):
    if start == end:
        return True
    mid = (start + end) // 2
    sign = True
    for i in range(start,mid):
        if status[i] == status[end-i]:
            sign = False
            break
    if sign:
        return origami(start, mid - 1) and origami(mid + 1, end)
    else:
        return False


for T in range(int(input())):
    status = list(map(int, input()))
    if origami(0, len(status) - 1):
        answer = 'YES'
    else:
        answer = 'NO'
    print(answer)

# 예제
# 9
# 1001110
# 0110001
# 0010110
# 100
# 001
# 011
# 110
# 000
# 0
