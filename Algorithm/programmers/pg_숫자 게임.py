# sort | programmers 숫자 게임
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    idx_a = 0
    idx_b = 0
    while True:
        if idx_a == len(A) or idx_b == len(B):
            break
        a, b = A[idx_a], B[idx_b]
        if b > a:
            answer += 1
            idx_a += 1
            idx_b += 1
            continue
        else:
            idx_b += 1

    return answer