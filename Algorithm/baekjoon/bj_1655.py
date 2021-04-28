# 우선순위큐 | bj 1655 가운데를 말해요
import sys
import heapq

# sys.setrecursionlimit(10 ** 9)
inp = sys.stdin.readline

N = int(inp())
left = []  # 왼쪽은 최대값이 mid로 올 수 있으니 최대힙으로
mid = None
right = []  # 오른쪽은 최소값이 mid로 올 수 있으니 최소힙으로
for _ in range(N):
    temp = int(inp())
    if mid is None:
        mid = temp
    elif temp < mid:  # 새로운 값이 mid보다 작으면 왼쪽삽입
        heapq.heappush(left, -temp)
        if len(right) < len(left):  # 만약 왼쪽에 삽입하고난 후에 왼쪽이 오른쪽보다 길면
            heapq.heappush(right, mid) # 왼쪽의 제일 큰값을 미드로 옮기고 미드는 오른쪽으로
            mid = -heapq.heappop(left)
    elif temp > mid:
        heapq.heappush(right, temp)
        if len(right) > len(left) + 1:
            heapq.heappush(left, -mid)
            mid = heapq.heappop(right)
    elif temp == mid:  # 같을때는 왼쪽 오른쪽 골고루 삽입
        if len(right) > len(left):
            heapq.heappush(left, -mid)
        else:
            heapq.heappush(right, mid)
    print(mid)
