# 트리 그래프 dfs | bj 1068 트리
# http://boj.kr/23fb5090565742c6964085ef1520aab6
import sys
# import itertools
# from math import factorial
# from collections import deque
# import heapq
# import math

# sys.setrecursionlimit(int(1e9))

def input():
    return sys.stdin.readline().rstrip()


n = int(input())
tree = {}
top_parent = -1
for idx, parent in enumerate(map(int, input().split())):
    if parent == -1:
        top_parent = idx
    else:
        tree[parent] = tree.get(parent, []) + [idx]

remove_num = int(input())
# 부모 노드를 삭제하는 경우
if top_parent == remove_num:
    print(0)
    sys.exit(0)

answer = 0
stack = [top_parent]
while stack:
    node = stack.pop()
    sign = False
    for n_node in tree.get(node, []):
        if n_node == remove_num:
            continue
        stack.append(n_node)
        sign = True
    if not sign:
        answer += 1
print(answer)
