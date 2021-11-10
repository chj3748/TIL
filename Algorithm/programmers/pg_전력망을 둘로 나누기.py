# dfs bfs | programmers 전력망을 둘로 나누기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(n, wires):
    answer = n
    elec_tower = [[] for _ in range(n + 1)]
    for wire_a, wire_b in wires:
        elec_tower[wire_a].append(wire_b)
        elec_tower[wire_b].append(wire_a)
    for i in range(n - 1):
        dont_a, dont_b = wires[i]
        if dont_a > dont_b:
            dont_a, dont_b = dont_b, dont_a
        visited = [0] * (n + 1)
        visited[1] = 1
        cnt = 1
        stack = [1]
        while stack:
            x = stack.pop()
            for nx in elec_tower[x]:
                if visited[nx]:
                    continue
                if x < nx:
                    if dont_a == x and dont_b == nx:
                        continue
                else:
                    if dont_b == x and dont_a == nx:
                        continue
                cnt += 1
                if cnt >= (n // 2 + answer):
                    stack = []
                    break
                visited[nx] = 1
                stack.append(nx)
        diff = abs(n - (cnt * 2))
        if answer > diff:
            answer = diff
    return answer