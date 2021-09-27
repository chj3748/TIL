# math 유클리드호제법 | programmers N개의 최소공배수
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def gcd(num1, num2):
    mod = 1
    while mod:
        mod = num1 % num2
        num1 = num2
        num2 = mod
    return num1

def lcm(num1, num2):
    return num1 * num2 // gcd(num1, num2)

def solution(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        curr = arr[i]
        if curr % temp == 0 or temp % curr == 0:
            temp = max(curr, temp)
        else:
            temp = lcm(temp, curr)
    return temp