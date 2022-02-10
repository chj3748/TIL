# 구현 우선순위큐 힙 해시 | baekjoon 21939 문제 추천 시스템 Version 1
# github.com/chj3748
import sys
import heapq
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
checked = defaultdict(int)
max_problems = []
min_problems = []
for i in range(N):
    p, l = map(int, input().split())
    checked[p] = l
    heapq.heappush(max_problems, [-l, -p])
    heapq.heappush(min_problems, [l, p])


def cmd(recommend):
    if recommend[0] == 'recommend':
        if recommend[1] == '1':
            while max_problems:
                l, p = map(lambda x : -x, max_problems[0])
                if not checked[p]:
                    heapq.heappop(max_problems)
                    continue
                if checked[p] != l:
                    heapq.heappop(max_problems)
                    continue
                print(p)
                break
        else:
            while min_problems:
                l, p = min_problems[0]
                if not checked[p]:
                    heapq.heappop(min_problems)
                    continue
                if checked[p] != l:
                    heapq.heappop(min_problems)
                    continue
                print(p)
                break

    elif recommend[0] == 'add':
        p, l = int(recommend[1]), int(recommend[2])
        checked[p] = l
        heapq.heappush(max_problems, [-l, -p])
        heapq.heappush(min_problems, [l, p])

    else:
        checked[int(recommend[1])] = 0


M = int(input())
for i in range(M):
    recommend = input().split()
    cmd(recommend)
