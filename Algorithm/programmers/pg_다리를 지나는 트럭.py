# stack que | programmers 다리를 지나는 트럭
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(bridge_length, weight, truck_weights):
    from collections import deque
    answer = 0
    trucks = deque(truck_weights)
    dq = deque()
    temp = 0
    while trucks or dq:
        answer += 1
        while True:
            if not dq:
                break
            if answer - dq[0][1] == bridge_length:
                truck = dq.popleft()[0]
                temp -= truck
            else:
                break
        if trucks and len(dq) < bridge_length:
            if temp + trucks[0] <= weight:
                temp += trucks[0]
                truck = trucks.popleft()
                dq.append([truck, answer])
    return answer

print(solution(2, 10, [7, 4, 5, 6]))