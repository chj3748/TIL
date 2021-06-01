# bf 백트래킹 | bj 10819 차이를 최대로
import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
numbers = list(map(int, input().split()))
used = [1] * N


def diff_sum(cnt, total, temp):
    global answer
    if cnt == N:
        if answer < total:
            answer = total
        return
    for i in range(N):
        if used[i]:
            used[i] = 0
            if cnt > 0:
                diff_sum(cnt + 1, total + abs(temp - numbers[i]), numbers[i])
            else:
                diff_sum(cnt + 1, total, numbers[i])
            used[i] = 1


answer = 0
diff_sum(0, 0, 0)
print(answer)
