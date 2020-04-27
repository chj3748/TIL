# card
n=int(input())
dic_num={}
many_card=-1
many_num=0
for _ in range(n):
    value=int(input())
    dic_num[value]=dic_num.get(value,0)+1
    if dic_num[value]>many_num:
        many_num=dic_num[value]
        many_card=value
    elif dic_num[value]==many_num:
        if value<many_card:
            many_card=value

print(many_card)
