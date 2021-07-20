# 문자열 | bj 9933 민균이의 비밀번호
# github.com/chj3748
# 좀 억지로 짜맞춘 풀이...?
import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
strings = defaultdict(int)
for _ in range(N):
    string = input()
    r_s = string[::-1]
    if r_s == string:
        print(len(string), string[len(string)//2])
    elif strings[string] or strings[r_s]:
        print(len(string), string[len(string)//2])
    else:
        strings[string] += 1