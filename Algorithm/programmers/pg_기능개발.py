# stack que | programmers 기능개발
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(progresses, speeds):
    answer = []
    from collections import deque
    dq_p = deque(progresses)
    dq_s = deque(speeds)
    while dq_p:
        cnt = 0
        for idx, speed in enumerate(dq_s):
            if dq_p[idx] == -1:
                continue
            dq_p[idx] += speed
        while dq_p:
            if dq_p[0] >= 100:
                dq_p.popleft()
                dq_s.popleft()
                cnt += 1
            else:
                break
        if cnt > 0:
            answer.append(cnt)
    return answer