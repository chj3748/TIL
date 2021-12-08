# bfs graph 재귀 | programmers 가장 먼 노드
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


sys.setrecursionlimit(20001)


def solution(n, edge):
    from collections import deque, defaultdict
    answer = 0
    checked = [0] * (n + 1)
    edges = defaultdict(list)
    for e in edge:
        n1, n2 = e
        edges[n1].append(n2)
        edges[n2].append(n1)

    checked[1] = 1

    def move_1(dq=deque([1])):
        nonlocal answer
        answer = len(dq)
        for i in range(answer):
            node_temp = dq.popleft()
            for next_node in edges[node_temp]:
                if checked[next_node]:
                    continue
                dq.append(next_node)
                checked[next_node] = 1
        if dq:
            move_1(dq)

    move_1()
    return answer