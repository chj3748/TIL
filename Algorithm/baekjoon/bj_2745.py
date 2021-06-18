# 수학 | bj 2745 진법 변환
import sys


def input():
    return sys.stdin.readline().rstrip()

N, B = input().split()
B = int(B)
answer = 0
alpha = {}
for c in range(65, 91):
    alpha[chr(c)] = c - 55
for n in range(10):
    alpha[str(n)] = n
for i in range(len(N)):
    num = N[i]
    temp = alpha[num]
    answer += temp * (B**(len(N) - i - 1))

print(answer)