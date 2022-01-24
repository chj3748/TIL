# 구현 | bj 20546 기적의 매매법
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
money_j = N
money_s = N
stock_j, stock_s = 0, 0
last_price = -1
updown = 0
cnt_continuous = 0
for price in list(map(int, input().split())):
    if price <= money_j:
        buy_stock, changes = divmod(money_j, price)
        stock_j += buy_stock
        money_j = changes
    if last_price == -1:
        last_price = price
        continue
    if price == last_price:
        updown = 0
        cnt_continuous = 0
    elif price > last_price:
        if updown == 1:
            cnt_continuous += 1
        else:
            updown = 1
            cnt_continuous = 1
    elif price < last_price:
        if updown == -1:
            cnt_continuous += 1
        else:
            updown = -1
            cnt_continuous = 1
    if cnt_continuous == 3:
        if updown == 1:
            money_s += price * stock_s
            stock_s = 0
        else:
            buy_stock, changes = divmod(money_s, price)
            stock_s += buy_stock
            money_s = changes
    last_price = price

money_j += last_price * stock_j
money_s += last_price * stock_s
if money_j > money_s:
    answer = 'BNP'
elif money_j < money_s:
    answer = 'TIMING'
else:
    answer = 'SAMESAME'
print(answer)