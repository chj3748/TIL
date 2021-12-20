# greedy union_find | programmers 섬 연결하기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(n, costs):
    import heapq
    answer = 0
    bridge = []
    for cost in costs:
        f, s, c = cost
        heapq.heappush(bridge, [c, f, s])

    parents = [i for i in range(n)]

    def find_parent(num):
        if parents[num] != num:
            parents[num] = find_parent(parents[num])
        return parents[num]

    def union_parents(num1, num2):
        p1, p2 = find_parent(num1), find_parent(num2)
        if p1 == p2:
            return False
        if p1 < p2:
            parents[p2] = p1
        else:
            parents[p1] = p2
        return True

    while bridge:
        c, f, s = heapq.heappop(bridge)
        if union_parents(f, s):
            answer += c
    return answer