# 우선순위큐 bf | bj 1202 보석 도둑
import sys
import heapq

# sys.setrecursionlimit(10 ** 9)
inp = sys.stdin.readline

N, K = map(int, inp().split())
jewels = [list(map(int, inp().split())) for _ in range(N)]
for _ in range(K):
    jewels.append([int(inp()), 1000001])  # 같은 무게를 갖는 보석보다 뒤에 정렬이 되어야하기때문에 가격 또한 보석 최대값 보다 크게

jewels.sort()
h = []  # 현재 보다 가벼운 녀석을 가격을 기준으로 넣을거임
prices = 0
for jewel in jewels:
    if jewel[1] == 1000001:  # 가방임 : 가방보다 가벼운 보석중 제일 비싼놈 구함
        if len(h):
            prices += -heapq.heappop(h)
    else:  # 보석이라면 가격순으로 삽입
        heapq.heappush(h, -jewel[1])

print(prices)
