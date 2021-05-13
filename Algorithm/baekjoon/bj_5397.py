# 덱 스택 | bj 5397 키로거
import sys


# import itertools
# from math import factorial
from collections import deque
# import heapq
# import math

# sys.setrecursionlimit(int(1e9))


def input():
    return sys.stdin.readline().rstrip()


T = int(input())
for test in range(T):
    # insert와 pop에서 시간이 오래걸림
    # answer = []
    # pointer = len(answer)
    # for string in input():
    #     if string == '<':
    #         if pointer > 1:
    #             pointer -= 1
    #     elif string == '>':
    #         if pointer < len(answer):
    #             pointer += 1
    #     elif string == '-':
    #         if len(answer) and pointer > 0:
    #             answer.pop(pointer - 1)
    #             pointer -= 1
    #     else:
    #         answer.insert(pointer, string)
    #         pointer += 1
    # print(''.join(answer))

    # 시간 초과 해결법 : 포인터를 기준으로 왼쪽과 오른쪽 구분
    answer_l = deque()
    answer_r = deque()
    for string in input():
        if string == '<':
            if answer_l:
                temp = answer_l.pop()
                answer_r.appendleft(temp)
        elif string == '>':
            if answer_r:
                temp = answer_r.popleft()
                answer_l.append(temp)
        elif string == '-':
            if answer_l:
                answer_l.pop()
        else:
            answer_l.append(string)
    print(''.join(answer_l + answer_r))
