# 5186
T=int(input())
for t in range(1,T+1):
    number= float(input())
    result=''
    while len(result)<13:
        temp= number*2
        head= temp/1
        number=temp-int(head)
        result+=str(int(head))
        if temp-int(head)==0:
            break
    if len(result)==13:
        result='overflow'
    print('#{} {}'.format(t, result))