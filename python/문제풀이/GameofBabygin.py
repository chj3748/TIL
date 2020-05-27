# 5203 베이비진게임
T=int(input())
for t in range(1,T+1):
    cards = list(map(int,input().split()))
    result=-1
    acount=[0]*10
    bcount=[0]*10
    idx=0
    while cards:
        card = cards.pop(0)
        if idx%2==0:
            acount[card]+=1
            if acount[card]==3:
                result=1
                break

            if card>=2:
                if acount[card-2]>0 and acount[card-1]>0:
                    result=1
                    break
            if card<=7:
                if acount[card+1]>0 and acount[card+2]>0:
                    result=1
                    break
            if card<=8 and card>=1:
                if acount[card+1]>0 and acount[card-1]>0:
                    result=1
                    break
        if idx%2==1:
            bcount[card]+=1
            if bcount[card]==3:
                result=2
                break
            if card>=2:
                if bcount[card-2]>0 and bcount[card-1]>0:
                    result=2
                    break
            if card<=7:
                if bcount[card+1]>0 and bcount[card+2]>0:
                    result=2
                    break
            if card<=8 and card>=1:
                if bcount[card+1]>0 and bcount[card-1]>0:
                    result=2
                    break
        idx+=1
    else:
        result=0

    print('#{} {}'.format(t,result))