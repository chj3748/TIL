# math 순열 조합 | programmers 줄 서는 방법
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def factorial(num):
    temp = 1
    for i in range(1, num + 1):
        temp *= i
    return temp


def solution(n, k):
    answer = []
    numbers = [i for i in range(21)]
    for i in range(n, 0, -1):
        div, mod = divmod(k - 1, factorial(i - 1))
        temp = numbers[div + 1]
        answer.append(temp)
        numbers.remove(temp)
        k -= factorial(i - 1) * (div)

    return answer