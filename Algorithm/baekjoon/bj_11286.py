# 우선순위큐 | bj 11286 절대값 힙
# github.com/chj3748
import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()


N = int(input())
hq = []
for _ in range(N):
    num = int(input())
    if num:
        heapq.heappush(hq, [abs(num), num])
    else:
        if hq:
            print_num = heapq.heappop(hq)
            print(print_num[1])
        else:
            print(0)