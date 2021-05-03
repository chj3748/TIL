# dfs 플로이드와샬? 그래프 | bj 2458 키순서
import sys

# import itertools
# from math import factorial
# from collections import deque

sys.setrecursionlimit(int(1e9))
inp = sys.stdin.readline

n, m = map(int, inp().split())

top_down = [[] for _ in range(n + 1)]
bottom_up = [[] for _ in range(n + 1)]
for _ in range(m):
    # a 학생의 키 < b 학생의 키
    a, b = map(int, inp().split())
    top_down[b].append(a)
    bottom_up[a].append(b)

answer = 0


# 기준 학생보다 키가 작은 학생을 전부 찾아내서 반환
def top_down_check(student):
    smaller = 0
    stack = []
    checked = []
    stack.append(student)
    while stack:
        someone = stack.pop()
        for next_student in top_down[someone]:
            if next_student not in checked:
                stack.append(next_student)
                checked.append(next_student)
                smaller += 1
    return smaller


# 기준학생보다 키가 큰 학생을 전부 찾아서 반환
def bottom_up_check(student):
    taller = 0
    stack = []
    checked = []
    stack.append(student)
    while stack:
        someone = stack.pop()
        for next_student in bottom_up[someone]:
            if next_student not in checked:
                stack.append(next_student)
                checked.append(next_student)
                taller += 1
    return taller


for i in range(1, n + 1):
    if top_down_check(i) + bottom_up_check(i) == n - 1:
        answer += 1

print(answer)
