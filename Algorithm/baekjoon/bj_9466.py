# dfs 그래프 | bj 9466 텀 프로젝트
import sys


def input():
    return sys.stdin.readline().rstrip()


def dfs(idx):
    stack = [idx]
    visited = [idx]
    cnt = 0
    while stack:
        num = stack.pop()
        nxt = choose[num]
        if checked[nxt]:
            while visited:
                member = visited.pop()
                checked[member] = -1
                cnt += 1
                if member == nxt:
                    return cnt
        else:
            if not checked[nxt]:
                visited.append(nxt)
                stack.append(nxt)
                checked[nxt] = 1
            else:
                return 0
    return 0


T = int(input())
for _ in range(T):
    n = int(input())
    total = n
    choose = [0] + list(map(int, input().split()))
    checked = [0] * (n + 1)
    for i in range(1, n + 1):
        if not checked[i]:
            checked[i] = 1
            total -= dfs(i)
    print(total)
