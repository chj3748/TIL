# 위상정렬 그래프 | bj 1516 게임 개발
import sys

# import itertools
# from math import factorial
# from collections import deque
# import heapq

# sys.setrecursionlimit(int(1e9))
inp = sys.stdin.readline

N = int(inp())
# N번 빌딩이 지어지는데 필요한 최단 시간 = max(선행건물 시간) + N건물 시간
build_time = [0] * (N + 1)  # 각 빌딩이 지어지는데 필요한 시간
build_mtime = [0] * (N + 1)  # 각 빌딩의 최소 총 필요 시간
need = [[] for _ in range(N + 1)]  # 각 빌딩의 선행건물

for building in range(1, N + 1):
    for idx, val in enumerate(map(int, inp().split())):
        if idx == 0:
            build_time[building] = val
        elif val != -1:
            need[building].append(val)


def find_time(building):
    if build_mtime[building] == 0:  # 빌딩이 완공된 적없다면 0
        total = build_time[building]  # 기본 완공시간은 각 빌딩의 건설시간
        temp = 0  # 선행건물 시간 중 최대값을 찾기위한 임시변수
        for n in need[building]:
            if temp < find_time(n):
                temp = find_time(n)
        build_mtime[building] = total + temp
    return build_mtime[building]  # 한번이라도 완공된 적있다면 바로 값 반환


for building in range(1, N + 1):
    print(find_time(building))

