# math | programmers 소수 찾기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(numbers):
    answer = 0
    from collections import defaultdict
    from itertools import permutations

    checked = defaultdict(int)
    permu = []
    numbers = list(numbers)
    for i in range(len(numbers)):
        permu += permutations(numbers, i + 1)

    def is_prime(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for p in permu:
        temp_num = int(''.join(p))
        if temp_num < 2:
            continue
        if checked[temp_num]:
            continue
        checked[temp_num] += 1
        if is_prime(temp_num):
            answer += 1

    return answer