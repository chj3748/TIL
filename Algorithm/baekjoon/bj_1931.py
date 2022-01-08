# greedy sort | 1931 회의실 배정
# github.com/chj3748
import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
books = []
for _ in range(N):
    s, e = map(int, input().split())
    heapq.heappush(books, [e, s])

cnt = 0
end_time = 0
while books:
    e, s = heapq.heappop(books)
    if s >= end_time:
        cnt += 1
        end_time = e

print(cnt)