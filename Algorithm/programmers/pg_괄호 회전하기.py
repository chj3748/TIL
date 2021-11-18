# stack | programmers 괄호 회전하기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(s):
    from collections import deque, defaultdict
    answer = 0
    bracket = defaultdict(str)
    bracket['('] = -1
    bracket['['] = -1
    bracket['{'] = -1
    bracket[')'] = '('
    bracket[']'] = '['
    bracket['}'] = '{'

    def is_correct(s, cnt):
        target = deque(s)
        target.rotate(-1 * (cnt + 1))
        stack = []
        while target:
            temp = target.popleft()
            bracket_type = bracket[temp]
            if not bracket_type:
                return 0
            if bracket_type == -1:
                stack.append(temp)
                continue
            else:
                if stack:
                    if stack.pop() == bracket_type:
                        continue
                return 0
        if stack:
            return 0
        return 1

    for i in range(len(s)):
        answer += is_correct(s, i)

    return answer