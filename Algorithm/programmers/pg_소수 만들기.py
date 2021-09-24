# 소수 | programmers 소수 만들기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def is_prime(n):
    for i in range(2, int(n**(1/2) + 1)):
        if not n % i:
            return False
    return True

def solution(nums):
    answer = 0
    from itertools import combinations
    for combi in combinations(nums, 3):
        if is_prime(sum(combi)):
            answer += 1
    return answer