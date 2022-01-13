# 문자열 | 10798 세로읽기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


words = [input() for _ in range(5)]
answer = []
max_l = max([len(words[i]) for i in range(5)])
for i in range(max_l):
    for j in range(5):
        if len(words[j]) >= i + 1:
            answer.append(words[j][i])

print(''.join(answer))