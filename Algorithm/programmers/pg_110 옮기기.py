# stack | programmers 110 옮기기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(s):
    answer = []
    for snum in s:
        stack = []
        cnt = 0
        for num in snum:
            if len(stack) >= 2 and num == '0' and stack[-1] == '1' and stack[-2] == '1':
                stack.pop()
                stack.pop()
                cnt += 1
            else:
                stack.append(num)
        one_cnt = 0
        while stack:
            if stack[-1] == '1':
                stack.pop()
                one_cnt += 1
            else:
                break
        stack.append('110' * cnt)
        stack.append('1' * one_cnt)
        answer.append(''.join(stack))
    return answer