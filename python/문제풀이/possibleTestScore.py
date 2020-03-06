for t in range(1,int(input())+1):
    n=int(input())
    score=list(map(int,input().split()))
    total=sum(score)
    possible=[0]*(total+1)
    possible[0]=1
    result=[0]
    for s in score:
        temp=[]
        for pl in range(total+1-s):
            if possible[pl]==1:
                if possible[pl+s]==0:
                    temp.append(pl+s)
        for tem in temp:
            possible[tem]=1
        result+=temp
    print('#{} {}'.format(t,len(result)))