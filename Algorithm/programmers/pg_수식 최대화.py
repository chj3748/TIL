# permutation stack regrex | programmers 수식 최대화
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(expression):
    from itertools import permutations
    answer = 0
    exp = []
    temp = ''
    for e in expression:
        if e in ('*', '+', '-'):
            exp.append(temp)
            exp.append(e)
            temp = ''
        else:
            temp += e
    exp.append(temp)

    permus = permutations(['*', '+', '-'], 3)
    for permu in permus:
        copy_exp = list(exp)
        stack = []
        for i in range(3):
            while copy_exp:
                e = copy_exp.pop(0)
                if e == permu[i]:
                    stack.append(str(eval(stack.pop() + e + copy_exp.pop(0))))
                else:
                    stack.append(e)
            copy_exp = stack
            stack = []
        if answer < abs(int(copy_exp[0])):
            answer = abs(int(copy_exp[0]))
    return answer