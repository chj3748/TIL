# tree class | bj 트리의 높이와 너비
import sys
import math

sys.setrecursionlimit(int(1e9))


def input():
    return sys.stdin.readline().rstrip()


class Node(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        self.total = [data,left,right]


def inorder(node, lev):
    global order, max_lev
    if max_lev < lev:
        max_lev = lev
    if node.left:
        inorder(tree[node.left], lev + 1)
    if levs[lev][0] > order:
        levs[lev][0] = order
    if levs[lev][1] < order:
        levs[lev][1] = order
    order += 1
    if node.right:
        inorder(tree[node.right], lev + 1)


N = int(input())
root = (1 << (N + 1)) - 2  # 비트연산자로 루트 찾기
tree = {}
for _ in range(N):
    parent, l, r = map(int, input().split())
    # 자식으로 등장한적있는 비트 끄기
    if l > 0:
        root &= ~(1 << l)
    else:
        l = None
    if r > 0:
        root &= ~(1 << r)
    else:
        r = None
    tree[parent] = Node(parent, l, r)

levs = [[10001, 0] for _ in range(N + 1)]
root = int(math.log(root, 2) + 0.5)
order = 1
max_lev = 1
inorder(tree[root], 1)

answer_lev = 0
answer = 0
for i in range(1, max_lev + 1):
    diff = levs[i][1] - levs[i][0] + 1
    if answer < diff:
        answer_lev = i
        answer = diff
print(answer_lev, answer)
