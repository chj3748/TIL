# 구현 트리 | bj 9934 완전 이진 트리
import sys


def input():
    return sys.stdin.readline().rstrip()


K = int(input())
tree = [[] for _ in range(K)]

nodes = list(map(int, input().split()))

start = 0
end = 2 ** K - 1
depth = 0


def binary(d, s, e):
    if d == K:
        return
    mid = (s + e) // 2
    tree[d].append(nodes[mid])
    binary(d + 1, s, mid - 1)
    binary(d + 1, mid + 1, e)


binary(depth, start, end)
for level in tree:
    print(*level)
