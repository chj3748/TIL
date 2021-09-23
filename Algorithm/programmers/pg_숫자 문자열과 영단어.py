# 문자열 regex stack | programmers 숫자 문자열과 영단어
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(s):
    from collections import defaultdict
    nums = defaultdict(lambda : -1)
    nums['zero'] = 0
    nums['one'] = 1
    nums['two'] = 2
    nums['three'] = 3
    nums['four'] = 4
    nums['five'] = 5
    nums['six'] = 6
    nums['seven'] = 7
    nums['eight'] = 8
    nums['nine'] = 9
    for i in range(10):
        nums[str(i)] = i

    result = 0
    temp = ''
    for string in s:
        temp += string
        if nums[temp] != -1:
            result = 10 * result + nums[temp]
            temp = ''
    return result


solution("one4seveneight")
