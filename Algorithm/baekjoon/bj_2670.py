# bf dp | 2670 연속부분최대곱
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
answer = [float(input()) for _ in range(N)]
for i in range(1, N):
    answer[i] = max(answer[i], answer[i] * answer[i - 1])

print(f'{max(answer):.3f}')