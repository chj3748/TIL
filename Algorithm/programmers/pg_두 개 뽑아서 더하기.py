# 조합 | programmers 두 개 뽑아서 더하기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(numbers):
    answer = set()
    while numbers:
        add_num = numbers.pop()
        if not numbers:
            break
        for num in numbers:
            answer.add(num + add_num)
    return sorted(list(answer))
