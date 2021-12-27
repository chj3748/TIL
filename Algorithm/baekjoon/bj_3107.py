# string | bj 3107 IPv6
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


total = 8
double_s = input().split(':')
n = len(double_s)
single_s = []
flag = False
for ds in double_s:
    if ds == '' and not flag:
        for _ in range(total - n + 1):
            single_s.append('0000')
        flag = True
    else:
        single_s.append(ds)
answer = []
for s in single_s:
    answer.append(('0000' + s)[-4:])
print(':'.join(answer))
