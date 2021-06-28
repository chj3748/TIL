# 문자열 | 16171 나는 친구가 적다(small)
import sys

def input():
    return sys.stdin.readline().rstrip()


string = ''.join([s for s in input() if not s.isnumeric()])
answer = 1 if input() in string else 0
print(answer)