# 조합 | bj 6603 로또
import sys
from itertools import combinations


def input():
    return sys.stdin.readline().rstrip()


while True:
    value = input()
    if not value:
        break
    k, *numbers = list(map(int, value.split()))
    answers = map(list, combinations(numbers, 6))
    for answer in map(sorted, answers):
        print(*answer)
    print()
