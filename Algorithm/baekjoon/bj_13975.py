# 우선순위큐 | bj 13975 파일 합치기 3
import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()


for t in range(1, int(input()) + 1):
    K = int(input())
    files = []
    for file in map(int, input().split()):
        heapq.heappush(files, file)
    answer = 0
    while len(files) > 1:
        file1 = heapq.heappop(files)
        file2 = heapq.heappop(files)
        answer += file1 + file2
        heapq.heappush(files, file1 + file2)
    print(answer)
