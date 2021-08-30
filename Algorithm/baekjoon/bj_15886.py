# 문자열 | bj 15886 내 선물을 받아줘 2
# github.com/chj3748
import sys
import re


def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = re.split(r'W+', input())
cnt = 0
for ele in arr:
    if ele:
        cnt += 1
print(cnt)
