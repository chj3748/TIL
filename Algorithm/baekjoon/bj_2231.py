# 문자열 | bj 2231 분해합
import sys


def input():
    return sys.stdin.readline().rstrip()


number = int(input())
for i in range(1, number):
    temp = i
    for n in str(i):
        temp += int(n)
    if temp == number:
        print(i)
        break
else:
    print(0)