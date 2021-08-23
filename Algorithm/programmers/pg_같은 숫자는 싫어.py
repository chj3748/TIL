# stack | programmers 같은 숫자는 싫어
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()

def solution(arr):
    answer = []
    for num in arr:
        answer.append(num) if not answer or answer[-1] != num else 0
    return answer