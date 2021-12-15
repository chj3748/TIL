# dp 누적합 | programmers 광고 삽입
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def make_second(t):
    hh, mm, ss = map(int, t.split(':'))
    return hh * 3600 + mm * 60 + ss


def make_str_time(t):
    temp = []
    for i in range(3):
        div, mod = divmod(t, 60 ** (2 - i))
        temp.append(('00' + str(div))[-2:])
        t = mod
    return ':'.join(temp)


def solution(play_time, adv_time, logs):
    l = make_second(play_time) + 1
    checked = [0] * l
    ad_l = make_second(adv_time)
    for log in logs:
        start_time, end_time = map(make_second, log.split('-'))
        checked[start_time] += 1
        checked[end_time] -= 1

    max_look = -1
    answer = 0

    for i in range(1, l):
        checked[i] += checked[i - 1]

    for i in range(1, l):
        checked[i] += checked[i - 1]
        if i < ad_l - 1:
            continue
        total_look = checked[i] - checked[i - ad_l]
        if total_look > max_look:
            max_look = total_look
            answer = i - (ad_l) + 1

    return make_str_time(answer)