# 문자열 | bj 1159 농구 경기
import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
cnt_li = [0] * 26
answer = []
for _ in range(N):
    if N < 5:
        break
    name = input()
    idx = ord(name[0]) - ord('a')
    cnt_li[idx] += 1
    if cnt_li[idx] == 5:
        answer.append(name[0])
        cnt_li[idx] = -9999

if not answer:
    answer = 'PREDAJA'
else:
    answer.sort()
print(''.join(map(str, answer)))
