# 우선순위큐 | programmers 선입 선출 스케줄링
# github.com/chj3748
import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


def solution(n, cores):
    l = len(cores)
    t = 0
    used = []
    for i in range(l):
        heapq.heappush(used, [t + cores[i], i])
        n -= 1
    while n > 0:
        end_t, i = heapq.heappop(used)
        heapq.heappush(used, [end_t + cores[i], i])
        n -= 1
        if n == 0:
            return i + 1
        if end_t > t:  # 끝난 시간이 현재시간보다 클때
            t = end_t