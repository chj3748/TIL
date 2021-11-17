# combination | programmers 후보키
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(relation):
    l = len(relation)
    n = len(relation[0])
    from collections import deque
    answer = 0
    possible = deque([str(num) for num in range(n)])
    useds = []

    def find_ck(ck):
        nonlocal answer
        idx = int(ck[-1])
        if idx >= n:
            return
        temp_ck_set = set()
        for row in range(l):
            temp_ck = '_'.join([relation[row][int(col)] for col in ck])
            temp_ck_set.add(temp_ck)
        if len(temp_ck_set) == l:
            for used in useds:
                for u in used:
                    if u in ck:
                        continue
                    else:
                        break
                else:
                    break
            else:
                answer += 1
                useds.append(ck)
                return False
        return_val = []
        for ni in range(idx + 1, n):
            return_val.append(ck + str(ni))
        return return_val

    while possible:
        ck = possible.popleft()
        return_val = find_ck(ck)
        if return_val:
            possible += return_val

    return answer