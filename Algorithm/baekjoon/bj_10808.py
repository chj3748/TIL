# 문자열 구현 | bj 10808 알파벳 개수
import sys

def input():
    return sys.stdin.readline().rstrip()


string = input()
alphas = [0] * 26
for s in string:
    alphas[ord(s) - ord('a')] += 1

print(' '.join(map(str, alphas)))
