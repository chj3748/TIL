# 문자열 해시맵 | bj 4358 생태학
import sys

# sys.setrecursionlimit(int(1e9))
inp = sys.stdin.readline

trees = {}
total = 0
try:
    for tree in sys.stdin:
        if tree.strip() == '':
            break
        tree = tree.strip()
        trees[tree] = trees.get(tree, 0) + 1
        total += 1
except:
    pass
finally:
    for tree in sorted(list(trees.keys())):
        print(f'{tree} {trees[tree] / total * 100:.4f}')
