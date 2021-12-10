# 재귀 반복문 dfs | programmers 다단계 칫솔 판매
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


## 탑다운 코드
# import sys
# sys.setrecursionlimit(10004)
# def solution(enroll, referral, seller, amount):
#     n = len(enroll) + 1 # 센터가 n - 1번
#     enroll_to_num = {} # key = 이름, value = idx
#     sons = [[] for _ in range(n)] # 각 판매원이 갖는 하위 판매원 번호
#     for idx, [en_name, ref_name] in enumerate(zip(enroll, referral)):
#         enroll_to_num[en_name] = idx
#         senior = (n - 1) if ref_name == '-' else enroll_to_num[ref_name]
#         sons[senior].append(idx)

#     profits = [0] * n
#     for name, sell in zip(seller, amount):
#         seller_num = enroll_to_num[name]
#         profits[seller_num] += sell * 100

#     def cal_profit(idx):
#         my_profit = [profits[idx]]
#         for son in sons[idx]:
#             son_profits = cal_profit(son)
#             for son_profit in son_profits:
#                 diff = int(son_profit * 0.1)
#                 if diff:
#                     profits[son] -= diff
#                     profits[idx] += diff
#                     my_profit.append(diff)

#         return my_profit

#     cal_profit(n - 1)
#     profits.pop()
#     return profits
## 바텀업 코드
def solution(enroll, referral, seller, amount):
    idx = {}
    n = len(enroll)
    for i in range(n):
        idx[enroll[i]] = [i, referral[i]]

    profits = [0] * n

    for i in range(len(seller)):
        seller_n, sell_m = seller[i], amount[i] * 100
        my_idx, senior = idx[seller_n]
        profits[my_idx] += sell_m

        while True:
            diff = int(sell_m * 0.1)
            if not diff:
                break
            profits[my_idx] -= diff
            if senior == '-':
                break
            next_idx, next_senior = idx[senior]
            profits[next_idx] += diff
            sell_m = diff
            my_idx, senior = next_idx, next_senior

    return profits