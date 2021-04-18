# 분류 비트마스킹 | bj 11723 집합

import sys
input = sys.stdin.readline
N = int(input())
# emp = [0]*21
# ful = [1]*21
# S = emp
#
# for _ in range(N):
#     do = input().split()
#     if len(do) == 1:
#         if do == 'all':
#             S = ful
#         elif do == 'empty':
#             S = emp
#     else:
#         d = int(do[1])
#         if do[0] == 'add':
#             if S[d]==0:
#                 S[d]=1
#         elif do[0] == 'remove':
#             if S[d]==1:
#                 S[d] = 0
#         elif do[0] == 'check':
#             print(S[d])
#         elif do[0] == 'toggle':
#             if S[d]==1:
#                 S[d]=0
#             else:
#                 S[d]=1

S = set()
for _ in range(N):
    do = input().strip().split()
    if len(do) == 1:
        if do[0] == 'all':
            S = set(range(1,21))
        else:
            S.clear()
    else:
        d = int(do[1])
        if do[0] == 'add' and d not in S:
            S.add(d)
        elif do[0] == 'remove':
            if d in S:
                S.remove(d)
        elif do[0] == 'check':
            if d in S:
                print(1)
            else:
                print(0)
        elif do[0] == 'toggle':
            if d in S:
                S.remove(d)
            else:
                S.add(d)
