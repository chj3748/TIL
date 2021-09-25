# string regex | programmers 신규 아이디 추천
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def is_prime(n):
    for i in range(2, int(n**(1/2) + 1)):
        if not n % i:
            return False
    return True


def solution(new_id):
    import re
    answer = []
    for string in new_id:
        if re.match(r'[a-zA-Z0-9-_.]', string):
            if not answer:
                answer.append(string.lower())
                continue
            if string == '.' and answer[-1] == '.':
                continue
            answer.append(string.lower())
    else:
        answer = ''.join(answer).strip('.')
        if not answer:
            answer = 'a'
        answer = answer[:15].rstrip('.')
        if len(answer) <= 2:
            answer += answer[-1] * (3 - len(answer))
    return answer