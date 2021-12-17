# heap 우선순위큐 | programmers 야근 지수
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(n, works):
    import heapq
    works = list(map(lambda x: -x, works))
    heapq.heapify(works)
    for _ in range(n):
        if not works:
            break
        temp = -heapq.heappop(works)
        temp -= 1
        if temp:
            heapq.heappush(works, -temp)

    answer = sum(map(lambda x: x ** 2, works))
    return answer