# math 재귀 메모이제이션 | programmers 피보나치 수
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


sys.setrecursionlimit(100001)
fibos = [0] * 100001
fibos[1] = 1


def fibo(num):
    if not num or fibos[num]:
        return fibos[num]
    fibos[num] = fibo(num - 2) + fibo(num - 1)
    return fibos[num]


def solution(n):
    return fibo(n) % 1234567

# # 재귀없는 피보나치
# def solution(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a + b
#     return a

