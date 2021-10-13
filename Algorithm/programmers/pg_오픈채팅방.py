# list | programmers 오픈채팅방
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(record):
    answer = []
    from collections import defaultdict
    users = defaultdict(lambda : [['']])
    for r in record:
        temp = r.split()
        cmd, E = temp[0], temp[1:]
        if cmd == 'Enter':
            users[E[0]][0][0] = E[1]
            answer.append([users[E[0]][0], '님이 들어왔습니다.'])
        elif cmd == 'Leave':
            answer.append([users[E[0]][0], '님이 나갔습니다.'])
        else:
            users[E[0]][0][0] = E[1]
    result = []
    for ans in answer:
        result.append(f'{ans[0][0]}{ans[1]}')
    return result