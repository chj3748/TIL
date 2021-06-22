# 수학 구현 | bj 2877 4와 7
import sys


def input():
    return sys.stdin.readline().rstrip()


k = int(input())
bin_num = bin(k + 1)
answer = ''
for s in bin_num[3:]:
    if s == '0':
        answer += '4'
    else:
        answer += '7'
print(answer)