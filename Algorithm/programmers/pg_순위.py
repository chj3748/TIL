# graph dfs bfs | programmers 순위
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(n, results):
    answer = 0
    winner = [[] for _ in range(n)]
    looser = [[] for _ in range(n)]
    for result in results:
        A, B = map(lambda x: x - 1, result)
        winner[A].append(B)
        looser[B].append(A)

    for i in range(n):
        stack = [i]
        cnt = 1
        checked = [0] * n
        while stack:
            x = stack.pop()
            for nx in winner[x]:
                if checked[nx]:
                    continue
                stack.append(nx)
                checked[nx] = 1
                cnt += 1
        stack = [i]
        while stack:
            x = stack.pop()
            for nx in looser[x]:
                if checked[nx]:
                    continue
                stack.append(nx)
                checked[nx] = 1
                cnt += 1
        if cnt == n:
            answer += 1
    return answer