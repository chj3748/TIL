def cal_prob(idx,temp_prob=100):
    global maxprob
    if temp_prob<maxprob:
        return
    if idx==n:
        maxprob=max(temp_prob, maxprob)
    else:
        for i in range(n):
            if visit[i]==0 and arr[idx][i] != 0:
                visit[i]=1
                cal_prob(idx+1,temp_prob*arr[idx][i])
                visit[i]=0


for t in range(1,int(input())+1):
    n = int(input())
    arr = [ [j/100 for j in map(int,input().split())] for i in range(n)]
    visit=[0]*n
    maxprob=0
    cal_prob(0)

    print('#{0} {1:.6f}'.format(t, maxprob))