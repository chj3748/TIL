# 우선순위큐 | bj 11000 강의실 배정
import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
lecture = []
for _ in range(N):
    heapq.heappush(lecture, list(map(int, input().split())))

end_points = []
while lecture:
    l = heapq.heappop(lecture)
    temp = []
    if end_points:
        if l[0] >= end_points[0]:
            heapq.heappop(end_points)
    heapq.heappush(end_points, l[1])


print(len(end_points))
