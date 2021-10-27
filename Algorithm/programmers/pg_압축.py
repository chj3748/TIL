# dict string | programmers 압축
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(msg):
    from collections import defaultdict, deque
    lzw_dict = defaultdict(int)
    for i in range(26):
        lzw_dict[chr(ord('A') + i)] = i + 1
    else:
        i = 27
    answer = []
    msg = deque(msg)
    temp = ''
    while msg:
        while msg:
            temp += msg[0]
            if lzw_dict[temp]:
                msg.popleft()
                continue
            else:
                lzw_dict[temp] = i
                i += 1
                break
        else:
            answer.append(lzw_dict[temp])
            continue
        answer.append(lzw_dict[temp[:-1]])
        temp = ''
    return answer