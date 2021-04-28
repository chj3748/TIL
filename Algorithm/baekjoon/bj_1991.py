# 트리 | bj 1991 트리 순회
import sys
import heapq

# sys.setrecursionlimit(10 ** 9)
inp = sys.stdin.readline

N = int(inp())
preorder = []  # 전위순회
inorder = []  # 중위순회
postorder = []  # 후위순회

tree = {}
for _ in range(N):
    parent, left, right = inp().split()
    tree[parent] = [left, right]


def move(start):
    preorder.append(start)
    if tree[start][0] != '.':
        move(tree[start][0])
    inorder.append(start)
    if tree[start][1] != '.':
        move(tree[start][1])
    postorder.append(start)


move('A')

print(''.join(preorder))
print(''.join(inorder))
print(''.join(postorder))
