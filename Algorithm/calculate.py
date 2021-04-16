# swea 5247 graph bfs 연산
from collections import deque
def calculate(N, M):
    global used
    q = deque()
    q.append([N, 0])
    while q:
        number, cnt = q.popleft()
        next_n1 = number + 1
        next_n2 = number - 1
        next_n3 = number * 2
        next_n4 = number - 10
        if M == next_n1:
            return cnt + 1
        if 0<next_n1 <= 1000000 and used[next_n1] == 0:
            q.append([next_n1, cnt + 1])
            used[next_n1] = 1
        if M == next_n2:
            return cnt + 1
        if 0<next_n2 <= 1000000 and used[next_n2] == 0:
            q.append([next_n2, cnt + 1])
            used[next_n2] = 1
        if M == next_n3:
            return cnt + 1
        if 0<next_n3 <= 1000000 and used[next_n3] == 0:
            q.append([next_n3, cnt + 1])
            used[next_n3] = 1
        if M == next_n4:
            return cnt + 1
        if 0<next_n4 <= 1000000 and used[next_n4] == 0:
            q.append([next_n4, cnt + 1])
            used[next_n4] = 1


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    global used
    used = [0]*1000001
    used[N] = 1
    result = calculate(N, M)
    print('#{} {}'.format(t, result))
