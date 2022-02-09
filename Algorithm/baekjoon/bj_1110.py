# math | baekjoon 1110 더하기 사이클
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
end = N
cnt = 0


def new_number(num):
    if num < 10:
        return num * 10 + num
    return (num % 10) * 10 + (num // 10 + num % 10) % 10


while True:
    cnt += 1
    N = new_number(N)
    if N == end:
        break

print(cnt)