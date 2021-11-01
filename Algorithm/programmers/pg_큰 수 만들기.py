# stack greedy | programmers 큰 수 만들기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


# 첫번째 풀이
def solution(number, k):
    from collections import deque
    stack = []
    number = deque(list(map(int, number)))
    while number and k > 0:
        num = number.popleft()
        if stack:
            while k > 0 and stack and stack[-1] < num:
                stack.pop()
                k -= 1
        if k > 0 and number and num < number[0]:
            k -= 1
            continue
        stack.append(num)

    for num in number:
        stack.append(num)

    for _ in range(k):
        stack.pop()
    return ''.join(map(str, stack))


# 두번째 풀이(개선안)
def solution(number, k):
    stack = []
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    return ''.join(stack[:len(stack) - k])