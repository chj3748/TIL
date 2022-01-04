# math | programmers 기능개발
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(progresses, speeds):
    answer = []
    days = 0
    n = len(progresses)
    for i in range(n):
        remained = 100 - progresses[i] - speeds[i] * days
        if remained > 0:
            more_d = remained // speeds[i]
            ceil_d = 1 if remained % speeds[i] else 0
            days += more_d + ceil_d
            answer.append(1)
        else:
            answer[-1] += 1
    return answer