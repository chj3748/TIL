# stack | bj 2504 괄호의 값
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


string = input()
stack = []
before_num = 0
pairs = {
    '(' : 2,
    '[' : 3,
    ')' : '(',
    ']' : '['
}
answer = 0
for val in string:
    if val == '(' or val == '[':
        stack.append(val)
    else:
        if stack:
            last = stack[-1]
            temp = []
            while stack:
                if type(last) == int:
                    temp.append(stack.pop())
                    if not stack:
                        print(0)
                        sys.exit(0)
                else:
                    break
                last = stack[-1]
            if pairs[val] == last:
                stack.pop()
                stack.append((sum(temp) if temp else 1)*pairs[last])
            else:
                answer = 0
                break
        else:
            answer = 0
            break
else:
    answer = 0
    for s in stack:
        if type(s) == int:
            answer += s
        else:
            answer = 0
            break

print(answer)