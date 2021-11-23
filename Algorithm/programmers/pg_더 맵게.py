# heap | programmers 더 맵게
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(scoville, K):
    import heapq
    answer = 0
    hq = []
    for food in scoville:
        heapq.heappush(hq, food)
    while len(hq) > 1:
        if hq[0] >= K:
            break
        answer += 1
        first_food = heapq.heappop(hq)
        second_food = heapq.heappop(hq)
        heapq.heappush(hq, first_food + second_food * 2)
    if hq[0] < K:
        answer = -1
    return answer