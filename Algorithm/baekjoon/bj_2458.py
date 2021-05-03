# dfs 플로이드와샬? 그래프 | bj 2458 키순서
import sys

# import itertools
# from math import factorial
# from collections import deque

# sys.setrecursionlimit(int(1e9))
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
    stack = [student]
    while stack:
        someone = stack.pop()
        for next_student in top_down[someone]:
            if not checked[next_student]:
                stack.append(next_student)
                checked[next_student] = 1
                smaller += 1
    return smaller


# 기준학생보다 키가 큰 학생을 전부 찾아서 반환
def bottom_up_check(student):
    taller = 0
    stack = [student]
    while stack:
        someone = stack.pop()
        for next_student in bottom_up[someone]:
            if not checked[next_student]:
                stack.append(next_student)
                checked[next_student] = 1
                taller += 1
    return taller


for i in range(1, n + 1):
    checked = [0]*(n+1)
    td_cnt = top_down_check(i)
    bu_cnt = bottom_up_check(i)
    if td_cnt + bu_cnt == n - 1:
        answer += 1

print(answer)


# 다른 풀이
## 훨씬 빠름
### 각 학생에서 키가 크던 작던 상관없이 깊이 탐색을 하면서
### 찾은 학생마다 +1을 해줌
### 그 결과 edge_cnt 테이블에는 각 학생이 몇번 호출 됐는지가 체크 됨
### 즉 본인 제외 모든 학생에게 호출된 학생은 모든 학생과 연결된 키순서가 있다는 것

# def dfs(start, cur):
#     if start != cur:
#         edge_cnt[start] += 1
#         edge_cnt[cur] += 1
#     visited[cur] = True
#     for w in graph[cur]:
#         if not visited[w]:
#             dfs(start, w)
#
#
# N, M = list(map(int, input().split()))
# graph = [[] for _ in range(N+1)]
# ans = 0
# for _ in range(M):
#     a, b = list(map(int, input().split()))
#     graph[a].append(b)
#
# edge_cnt = [0] * (N+1)
# for node in range(1, N+1):
#     visited = [False] * (N+1)
#     dfs(node, node)
#
# for node in range(1, N+1):
#     if edge_cnt[node] == N-1:
#         ans += 1
#
# print(ans)
