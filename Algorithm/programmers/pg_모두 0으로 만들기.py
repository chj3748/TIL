# tree dfs bfs | programmers 모두 0으로 만들기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(a, edges):
    from collections import defaultdict
    if sum(a):
        return -1
    edge = [[] for _ in range(len(a))]
    incount = defaultdict(int)
    for e in edges:
        f, s = e
        edge[f].append(s)
        edge[s].append(f)
        incount[f] += 1
        incount[s] += 1
    stack = []
    for k, v in incount.items():
        if v == 1:
            stack.append(k)

    removed = [0] * len(a)
    total_cnt = 0
    while stack:
        remove_node = stack.pop()
        next_node = -1
        for n_r_node in edge[remove_node]:
            if removed[n_r_node]:
                continue
            next_node = n_r_node
            break
        if a[remove_node] != 0 and next_node == -1:
            return -1
        if next_node != -1:
            temp = a[remove_node]
            a[remove_node] = 0
            a[next_node] += temp
            total_cnt += abs(temp)
            incount[next_node] -= 1
            incount[remove_node] -= 1
            if incount[next_node] == 1:
                stack.append(next_node)
        removed[remove_node] = 1
    return total_cnt