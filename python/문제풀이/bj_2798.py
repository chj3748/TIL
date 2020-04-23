def dp(idx, sum):
    global m,maxsum
    if sum<=m:
        if idx==3:
            maxsum=max(maxsum,sum)
            return
        for i in range(n):
            if used[i]==0:
                used[i]=1
                dp(idx+1,sum+cards[i])
                used[i]=0
    else:
        return



n, m = map(int,input().split())
cards=list(map(int,input().split()))
used=[0]*n
maxsum = 0
dp(0,0)

print(maxsum)