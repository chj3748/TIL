# 우선순위큐 | bj 17503 맥주 축제
# github.com/chj3748
import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


N, M, K = map(int, input().split())
bears = []
for _ in range(K):
    fav, lev = map(int, input().split())
    heapq.heappush(bears, [lev, fav])

total_fav = 0
drink_li = []
my_lev = 0
while bears:
    if len(drink_li) == N and total_fav >= M:
        break
    if len(drink_li) >= N:
        remove_fav = heapq.heappop(drink_li)
        total_fav -= remove_fav
    lev, fav = heapq.heappop(bears)
    heapq.heappush(drink_li, fav)
    total_fav += fav
    my_lev = lev

if len(drink_li) == N and total_fav >= M:
    print(my_lev)
else:
    print(-1)