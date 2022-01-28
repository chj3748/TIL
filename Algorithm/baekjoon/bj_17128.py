# math | baekjoon 17128 소가 정보섬에 올라온 이유
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


N, Q = map(int, input().split())
cows = list(map(int, input().split()))
num_Q = list(map(int, input().split()))
first_s = [cows[0] * cows[-1] * cows[-2] * cows[-3]]
total_s = first_s[0]
for i in range(1, N):
    temp = first_s[-1] // cows[i - 4] * cows[i]
    first_s.append(temp)
    total_s += temp
for q_i in range(Q):
    idx = num_Q[q_i] - 1
    for i in range(idx, idx + 4):
        i_4 = (N + i) % N
        first_s[i_4] *= -1
        total_s += 2 * first_s[i_4]
    print(total_s)