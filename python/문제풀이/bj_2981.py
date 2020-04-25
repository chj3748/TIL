import math

def divisor(num):
    divisors =[]
    length = int(math.sqrt(num))+1

    for i in range(1,length):
        if num%i ==0:
            divisors.append(i)
            if (num//i) not in divisors:
                divisors.append(num//i)
    divisors.sort()
    return divisors
n=int(input())
numlist=[]
for _ in range(n):
    numlist.append(int(input()))

numlist.sort(reverse=True)
dlist=[]
g=numlist[0]-numlist[1]
for idx in range(n-1):
    v=numlist[idx]-numlist[idx+1]
    dlist.append(v)
    g=math.gcd(v,g)

result=divisor(g)
print(' '.join(map(str,result[1:])))

