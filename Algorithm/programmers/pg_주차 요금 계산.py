# hash math | programmers 주차 요금 계산
# github.com/chj3748
import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def hh_to_mm(t):
    hh, mm = map(int, t.split(':'))
    return hh * 60 + mm


max_time = 23 * 60 + 59


def solution(fees, records):
    answer = []
    cars = defaultdict(lambda: [-1, 0])

    def cal_fee(t):
        if t <= fees[0]:
            return fees[1]
        more_t, less_t = divmod(t - fees[0], fees[2])
        if less_t:
            more_t += 1
        return fees[1] + fees[3] * more_t

    for record in records:
        t, car, status = record.split()
        car = int(car)
        t = hh_to_mm(t)
        if status == 'IN':
            cars[car][0] = t
        else:
            start_t = cars[car][0]
            cars[car][1] += t - start_t
            cars[car][0] = -1

    for car_num in sorted(cars.keys()):
        if cars[car_num][0] != -1:
            cars[car_num][1] += max_time - cars[car_num][0]
        answer.append(cal_fee(cars[car_num][1]))

    return answer
