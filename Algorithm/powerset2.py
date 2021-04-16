def construct_candidates(c):
    c[0]=True
    c[1]=False
    return 2


def backtrack(a, k, input):
    c = [0] * 2
    if k == input:
        li=[]
        for i in range(len(a)):
            if a[i] ==True:
                li.append(i)
        if sum(li)==10:
            print(li)
    else:
        nc = construct_candidates(c)
        k += 1
        for i in range(nc):
            a[k] = c[i]
            backtrack(a, k, input)
maxcandidates =2
nmax = 11
a= [0]*nmax
# s1=[0,1,2,3,4,5,6,7,8,9,10]
backtrack(a,0,10)

