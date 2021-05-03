# 집합 분리집합 서로소 집합 union-find| bj 1717 집합의 표현
import sys

# import itertools
# from math import factorial
# from collections import deque

sys.setrecursionlimit(int(1e9))
inp = sys.stdin.readline

n, m = map(int, inp().split())
parents = [i for i in range(n + 1)]  # 부모를 표현하는 리스트


# x의 최상위 부모를 찾아서 반환
def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]


# a와 b 의 최상위 부모를 일치해 줌으로써 집합을 합침
# 단 최상위 부모만 바꿀게아니라 상위 부모의 부모도 변경해줘야 예외가 발생하지않음
# ex) 1과 3을 합치고, 6과 7을 합친후 1과 7을 합치면 7의 부모만 1로 변해서
#       6의 부모는 6인상태로 혼자만 단절되는 경우가 생길 수 있는데
#       6의 부모도 1로 변경해줌으로써 6과 7 둘다 1과 같은 집합에 포함되게 함
def union_parent(a, b):
    parent_a = find_parent(a)
    parent_b = find_parent(b)
    if parent_a < parent_b:
        parents[parent_b] = parent_a  # 현재 최상위 부모의 부모를 변경해주는 과정
    elif parent_a > parent_b:
        parents[parent_a] = parent_b


for _ in range(m):
    case, el1, el2 = map(int, inp().split())
    if not case:
        union_parent(el1, el2)
    elif case:  # 만약 두 최상위 부모가 같으면 같은집합
        r_parent_el1 = find_parent(el1)
        r_parent_el2 = find_parent(el2)
        if r_parent_el1 == r_parent_el2:
            print('YES')
        else:
            print('NO')
