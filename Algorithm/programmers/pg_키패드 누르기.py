# 구현 | programmers 키패드 누르기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(numbers, hand):
    answer = []
    p_list = {
        1: [-1, 3],
        2: [0, 3],
        3: [1, 3],
        4: [-1, 2],
        5: [0, 2],
        6: [1, 2],
        7: [-1, 1],
        8: [0, 1],
        9: [1, 1],
        0: [0, 0],
    }
    l_position = [-1, 0]
    r_position = [1, 0]

    def is_left_right(num):
        nonlocal l_position, r_position
        if num in [1, 4, 7]:
            return 'L'
        if num in [3, 6, 9]:
            return 'R'
        l_dist = abs(l_position[0] - p_list[num][0]) + abs(l_position[1] - p_list[num][1])
        r_dist = abs(r_position[0] - p_list[num][0]) + abs(r_position[1] - p_list[num][1])
        if l_dist == r_dist:
            return -1
        if l_dist > r_dist:
            return 'R'
        else:
            return 'L'

    for number in numbers:
        result = is_left_right(number)
        if result == -1:
            result = 'R' if hand == 'right' else 'L'
        answer.append(result)
        if result == 'R':
            r_position = p_list[number]
        else:
            l_position = p_list[number]

    return ''.join(answer)