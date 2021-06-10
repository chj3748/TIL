# 그래프 dfs | bj 13023 ABCDE
import sys


def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
linked = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    linked[a].append(b)
    linked[b].append(a)
answer = 0
checked = [0] * N


def dfs(cnt, idx):
    global answer
    if answer:
        return
    if cnt == 4:
        answer = 1
        return
    checked[idx] = 1
    for next_idx in linked[idx]:
        if not checked[next_idx]:
            dfs(cnt + 1, next_idx)
            checked[next_idx] = 0


for number in range(N):
    if answer:
        break
    dfs(0, number)
    checked[number] = 0

print(answer)
