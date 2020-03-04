# ### 1
# def cal_price(price,idx):
#     global result
#     if price>result:
#         return
#     if (idx >= l):
#         result=min(result,price)
#     else:
#         if (pay[0] > 0):
#             pay[0] -= 1
#             cal_price(price + swimday[idx]*d, idx + 1)
#             pay[0] += 1
#         if (pay[1] > 0):
#             pay[1] -= 1
#             cal_price(price + m, idx + 1)
#             pay[1] += 1
#         if (pay[2] > 0):
#             pay[2] -= 1
#             cal_price(price + m3, idx + 3)
#             pay[2] += 1
# for t in range(1,int(input())+1):
#     d, m, m3, y = map(int,input().split())
#     result=y
#     swimday=list(map(int,input().split()))
#     while swimday[0]==0:
#         swimday.pop(0)
#     while swimday[-1]==0:
#         swimday.pop()
#     l=len(swimday)
#     pay=[l,l,(l//3)+1]
#     cal_price(0,0)
#     print('#{} {}'.format(t, result))


### 2
def cal_price(price,idx):
    global result
    if price>result:
        return
    if (idx >= l):
        result=min(result,price)
    elif swimday[idx]!=0:
        cal_price(price + swimday[idx]*d, idx + 1)
        cal_price(price + m, idx + 1)
        cal_price(price + m3, idx + 3)
    else:
        cal_price(price,idx+1)


for t in range(1,int(input())+1):
    d, m, m3, y = map(int,input().split())
    result=y
    swimday=list(map(int,input().split()))
    l=12
    cal_price(0,0)
    print('#{} {}'.format(t, result))