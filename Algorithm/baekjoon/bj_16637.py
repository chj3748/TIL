# 브루트포스 | bj 16637 괄호 추가하기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
expression = list(input())

max_val = -float('inf')


def cal_num(n1, n2, op):
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '*':
        return n1 * n2


def cal_add_bracket(idx, val):
    global max_val
    if idx >= len(expression):
        if max_val < val:
            max_val = val
        return
    op1 = expression[idx]
    num1 = int(expression[idx + 1])
    cal_add_bracket(idx + 2, cal_num(val, num1, op1))
    if idx + 3 >= len(expression):
        return
    op2 = expression[idx + 2]
    num2 = int(expression[idx + 3])
    cal_add_bracket(idx + 4, cal_num(val, cal_num(num1, num2, op2), op1))


start = int(expression[0])
cal_add_bracket(1, start)

print(max_val)
